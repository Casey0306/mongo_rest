class Utils:

    def dict_parser(self, dict_json_params):
        dict_json_result = {}
        for key_json in dict_json_params:
            if "collection" not in key_json:
                if isinstance(dict_json_params[key_json], str):
                    dict_json_result[key_json] = dict_json_params[key_json]
                elif isinstance(dict_json_params[key_json], dict) \
                        and len(dict_json_params[key_json]) == 1:
                    dict_json_result[key_json] = dict_json_params[key_json]
                elif isinstance(dict_json_params[key_json], dict):
                    for key_params, value_params in dict_json_params[key_json].items():
                        keyres = key_json + "." + key_params
                        dict_json_result[keyres] = value_params
                else:
                    dict_json_result = {}
        return dict_json_result
