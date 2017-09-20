import requests
import json


class SwagRequest:
    """
    SwagRequest provides automated creation of objects for request calls using the swagger json documentation of the
    destination API.
    """

    def __init__(self, method, target_url, parameters, swagger_url):
        """
        Constructor arguments are used to generate the correct request object for the provided target endpoint.
        :param method: Request method ('GET', 'POST', etc... )
        :param target_url: Target API endpoint.
        :param parameters: Parameters provided as a dictionary, used to match up API endpoint variables.
        :param swagger_url: URL for the swagger API documentation json
        """
        self.swagger_docs = self.get_swagger_docs(swagger_url=swagger_url)
        self.target_url = target_url
        self.parameters = parameters
        self.method = self.valid_methods(method)
        self.request_object = {}
        if method == "POST":
            self.construct_post_request(self.get_target_schema())
        else:
            # TODO: Implement construction methods for other HTTP methods
            raise NotImplemented

    def set_request_object(self, parameters):
        """
        Set the request object from an existing object.
        :param parameters: Request object
        :return:
        """
        self.request_object = parameters

    @staticmethod
    def get_swagger_docs(swagger_url):
        """
        Gets the swagger documentation json from the provided url.
        :param swagger_url: Url for swagger json
        :return:
        """
        try:
            swagger_json = requests.request("GET", url=swagger_url)
        except Exception as ex:
            # TODO: Narrow exception for specific http errors
            print(ex)
            return ""
        return json.loads(swagger_json.text)

    def get_target_schema(self):
        """
        Gets the schema from the swagger json.
        :return: Schema object
        """
        if self.target_url == "" or self.swagger_docs == "" or self.method == "":
            raise ValueError("ERROR: error found in one or more required SwaggerReader variables.")
        relative_api_endpoint = self.target_url.split(self.swagger_docs['basePath'], 1)[1]
        try:
            target_schema_path = list(
                self.swagger_docs['paths'][relative_api_endpoint][self.method]['parameters'][0]['schema'].values())
        except Exception as ex:
            print("ERROR: " + self.method + " method not found for " + self.target_url)
            print(ex)
            return None
        return self.get_definition(target_schema_path[0])

    @staticmethod
    def valid_methods(method):
        """
        Checks the method provided in the argument against a list of valid methods.
        :param method: HTTP request method
        :return: Method if valid or '' if not valid
        """
        valid_methods_list = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']
        return method.lower() if method.upper() in valid_methods_list else ''

    def get_definition(self, ref):
        """
        Get the definition from the reference path.
        :param ref: Path for the definition object
        :return: Swagger definition of reference path object
        """
        reference_parts = ref.split('#')[1].split('/')
        return self.swagger_docs[reference_parts[1]][reference_parts[2]]

    def construct_post_request(self, schema):
        """
        Construct POST request object from schema and parameters dictionary.
        :param schema: Schema for the specified API endpoint
        :return:
        """
        if len(self.parameters) == 0:
            return "ERROR: No parameters provided for request."
        if "properties" in schema:
            param_keys = [k.lower() for k in list(self.parameters.keys())]
            for item in schema["properties"].items():
                if item[0].lower() in param_keys:
                    if "type" in item[1]:
                        key = self.parameter_in_keys(self.parameters, item[0])
                        self.request_object[item[0]] = self.parameters[key]
                    elif "$ref" in item[1]:
                        self.request_object[item[0]] = self.construct_post_request_recur(self.get_definition(item[1]["$ref"]))
                elif "$ref" in item[1]:
                    if item[0] in self.request_object:
                        self.request_object[item[0]].append(self.construct_post_request_recur(self.get_definition(item[1]["$ref"])))
                    else:
                        self.request_object[item[0]] = self.construct_post_request_recur(self.get_definition(item[1]["$ref"]))
                else:
                    print(item[0] + " parameter not found in provided object.")

    def construct_post_request_recur(self, schema):
        """
        Recursive POST request object method, iterates through schema until at leaf.
        :param schema: Schema of custom object, defined within swagger json docs
        :return: Dictionary of the resulting keys and parameter values
        """
        params = {}
        for item in schema["properties"].items():
            param_keys = [k.lower() for k in list(self.parameters.keys())]
            if item[0].lower() in param_keys:
                if "type" in item[1]:
                    key = self.parameter_in_keys(self.parameters, item[0])
                    params[item[0]] = str(self.parameters[key])
                elif "$ref" in item[1]:
                    params[item[0]] = self.construct_post_request_recur(self.get_definition(item[1]["$ref"]))
            elif "$ref" in item[1]:
                params[item[0]] = self.construct_post_request_recur(self.get_definition(item[1]["$ref"]))
            else:
                print(item[0] + " parameter not found in provided object.")
        return params

    @staticmethod
    def parameter_in_keys(parameters, key):
        """
        Compares parameter names and keys, case insensitive.
        :param parameters: Dictionary of parameters provided for request
        :param key: Specific key of the current key-value pair being constructed
        :return: Key from the parameters object that matches the key in the schema
        """
        for p in parameters.keys():
            if p.casefold() == key.casefold():
                return p
        return "ERROR: Key not found in parameters."
