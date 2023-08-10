from exceptions.datatype_exceptions import CollectiveDataTypeError
from database.TypeChecker import TypeChecker


def serialize_data(schema_config, req_body):
    serialized_object = {}

    for key, schema_descriptor in schema_config.items():
        if schema_descriptor.get("type") == "string":
            serialized_object[key] = req_body.value.get(key)
        elif schema_descriptor.get("type") == "bool":
            if req_body.value.get(key).lower() == "true":
                serialized_object[key] = True
            elif req_body.value.get(key).lower() == "false":
                serialized_object[key] = False
        elif schema_descriptor.get("type") in ["int",
                                               "bigint",
                                               "number",
                                               "email",
                                               "timestamp"]:
            serialized_object[key] = req_body.value.get(key)

    return serialized_object


def validate_data(schema_config, req_body):
    typechecker = TypeChecker()

    for key, schema_descriptor in schema_config.items():
        if schema_descriptor.get("type") == "string":
            status, problems = typechecker.is_valid_string(key,
                                                           req_body.value.get(key),
                                                           schema_descriptor)

            if status is False:
                raise CollectiveDataTypeError(problems)
        elif schema_descriptor.get("type") == "int":
            status, problems = typechecker.is_valid_int(key,
                                                        req_body.value.get(key),
                                                        schema_descriptor)
            if status is False:
                raise CollectiveDataTypeError(problems)
        elif schema_descriptor.get("type") == "bigint":
            status, problems = typechecker.is_valid_big_int(key,
                                                            req_body.value.get(key),
                                                            schema_descriptor)

            if status is False:
                raise CollectiveDataTypeError(problems)
        elif schema_descriptor.get("type") == "bool":
            status, problems = typechecker.is_valid_bool(key,
                                                         req_body.value.get(key),
                                                         schema_descriptor)

            if status is False:
                raise CollectiveDataTypeError(problems)
        elif schema_descriptor.get("type") == "number":
            status, problems = typechecker.is_valid_number(key,
                                                           req_body.value.get(key),
                                                           schema_descriptor)

            if status is False:
                raise CollectiveDataTypeError(problems)
        elif schema_descriptor.get("type") == "email":
            status, problems = typechecker.is_valid_email(key,
                                                          req_body.value.get(key),
                                                          schema_descriptor)
            if status is False:
                raise CollectiveDataTypeError(problems)
        elif schema_descriptor.get("type") == "timestamp":
            status, problems = typechecker.is_valid_timestamp(key,
                                                              req_body.value.get(key),
                                                              schema_descriptor)

            if status is False:
                raise CollectiveDataTypeError(problems)
