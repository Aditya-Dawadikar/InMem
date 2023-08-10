import re
from exceptions.datatype_exceptions import DataTypeError

class TypeChecker:
    def __init__(self):
        pass
    
    def check_null_allowed(self, field, value, schema_descriptor):
        if schema_descriptor.get("null_allowed") is not None:
            # Checking is_null before other checks
            if schema_descriptor.get("null_allowed") is False and \
                value is None:
                    return {
                        "field": field,
                        "null_allowed": schema_descriptor.get("null_allowed"),
                        "received_value": value
                    }
            return None
    
    def is_valid_string(self, field, value, schema_descriptor):
        identified_problems = []
        
        check_null_allowed_res = self.check_null_allowed(
                                                            field,
                                                            value,
                                                            schema_descriptor
                                                        )
        if check_null_allowed_res is not None:
            identified_problems.append(check_null_allowed_res)
        else:
            if value is not None:
                if not isinstance(value, str):
                    # If given item is not string, then return
                    identified_problems.append(
                        {
                            "field": field,
                            "is_string": False,
                            "received_value": value
                        }
                    )
                    return False, identified_problems
                else:   
                    if schema_descriptor.get("max_length") is not None:
                        if len(value) > schema_descriptor.get("max_length"):
                            identified_problems.append(
                                {
                                    "field": field,
                                    "expected_max_length": schema_descriptor.get("max_length"),
                                    "received_value": value
                                }
                            )
                    if schema_descriptor.get("min_length") is not None:
                        if len(value) < schema_descriptor.get("min_length"):
                            identified_problems.append(
                                {
                                    "field": field,
                                    "expected_min_length": schema_descriptor.get("min_length"),
                                    "received_value": value
                                }
                            )
                    if schema_descriptor.get("pattern") is not None:
                        if not re.fullmatch(schema_descriptor.get("pattern"), value):
                            identified_problems.append(
                                {
                                    "field": field,
                                    "pattern": schema_descriptor.get("pattern"),
                                    "received_value": value
                                }
                            )
                
                    if len(identified_problems)>0:
                        return False, identified_problems
            return True, None
    
    def is_valid_bool(self, field, value, schema_descriptor):
        identified_problems = []
        
        check_null_allowed_res = self.check_null_allowed(
                                                            field,
                                                            value,
                                                            schema_descriptor
                                                        )
        if check_null_allowed_res is not None:
            identified_problems.append(check_null_allowed_res)
        else:
            if value is not None:
                if not value.lower() in ["true","false"]:
                    identified_problems.append(
                        {
                            "field": field,
                            "expected_bool_string_representation": ["true", "false"],
                            "received_value": value
                        }
                    )

                if len(identified_problems)>0:
                    return False, identified_problems
        
        return True, None
    
    def is_valid_int(self, field, value, schema_descriptor):
        identified_problems = []
        
        check_null_allowed_res = self.check_null_allowed(
                                                            field,
                                                            value,
                                                            schema_descriptor
                                                        )
        if check_null_allowed_res is not None:
            identified_problems.append(check_null_allowed_res)
        else:
            if value is not None:
                if not isinstance(value, int):
                    identified_problems.append({
                        "field": field,
                        "error": "Expected an integer value",
                        "received_value": value
                    })
                
                if value<-2147483648 or value>2147483647:
                    identified_problems.append({
                        "field": field,
                        "expected_int_range": [-2147483648, 2147483647],
                        "received_value": value
                    })

                if schema_descriptor.get("max_value") is not None:
                    if value>schema_descriptor.get("max_value"):
                        identified_problems.append({
                            "field": field,
                            "expected_max_value": schema_descriptor.get("max_value"),
                            "received_value": value
                        })
                if schema_descriptor.get("min_value") is not None:
                    if value<schema_descriptor.get("min_value"):
                        identified_problems.append({
                            "field": field,
                            "expected_min_value": schema_descriptor.get("min_value"),
                            "received_value": value
                        })
                
                if identified_problems:
                    return False, identified_problems
        
        return True, None
        
    
    def is_valid_big_int(self, field, value, schema_descriptor):
        identified_problems = []
        
        check_null_allowed_res = self.check_null_allowed(
            field, value, schema_descriptor
        )
        if check_null_allowed_res:
            identified_problems.append(check_null_allowed_res)
        else:
            if value is not None:
                if not isinstance(value, int):
                    identified_problems.append({
                        "field": field,
                        "error": "Expected an integer value",
                        "received_value": value
                    })
                
                if value<-9223372036854775808 or value>9223372036854775807:
                    identified_problems.append({
                        "field": field,
                        "expected_big_int_range": [-9223372036854775808, 9223372036854775807],
                        "received_value": value
                    })
                    
                if schema_descriptor.get("max_value") is not None:
                    if value>schema_descriptor.get("max_value"):
                        identified_problems.append({
                            "field": field,
                            "expected_max_value": schema_descriptor.get("max_value"),
                            "received_value": value
                        })
                if schema_descriptor.get("min_value") is not None:
                    if value<schema_descriptor.get("min_value"):
                        identified_problems.append({
                            "field": field,
                            "expected_min_value": schema_descriptor.get("min_value"),
                            "received_value": value
                        })
                
                if identified_problems:
                    return False, identified_problems
        
        return True, None
    
    def is_valid_number(self, field, value, schema_descriptor):
        identified_problems = []
        
        check_null_allowed_res = self.check_null_allowed(
            field, value, schema_descriptor
        )
        if check_null_allowed_res:
            identified_problems.append(check_null_allowed_res)
        else:
            if value is not None:
                if not isinstance(value, (int, float)):
                    identified_problems.append({
                        "field": field,
                        "error": "Expected a numeric value",
                        "received_value": value
                    })
                    return False, identified_problems

                if value< -1.7976931348623157e+308 or value> 1.7976931348623157e+308:
                    identified_problems.append({
                        "field": field,
                        "expected_number_range": [-1.7976931348623157e+308, 1.7976931348623157e+308],
                        "received_value": value
                    })
                
                if schema_descriptor.get("max_value") is not None:
                    if value>schema_descriptor.get("max_value"):
                        identified_problems.append({
                            "field": field,
                            "expected_max_value": schema_descriptor.get("max_value"),
                            "received_value": value
                        })
                if schema_descriptor.get("min_value") is not None:
                    if value<schema_descriptor.get("min_value"):
                        identified_problems.append({
                            "field": field,
                            "expected_min_value": schema_descriptor.get("min_value"),
                            "received_value": value
                        })
                
                if identified_problems:
                    return False, identified_problems
        
        return True, None
    
    def is_valid_email(self, field, value, schema_descriptor):
        check_null_allowed_res = self.check_null_allowed(
            field,
            value,
            schema_descriptor
        )
        if check_null_allowed_res is not None:
            identified_problems.append(check_null_allowed_res)
            return False, identified_problems
        else:
            if value is not None:
                email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"
                if not re.fullmatch(email_regex, value):
                    identified_problems.append(
                        {
                            "field": field,
                            "pattern": "valid_email",
                            "received_value": value
                        }
                    )
                
                if len(identified_problems) > 0:
                    return False, identified_problems
                
        return True, None
    
    def is_valid_timestamp(self, field, value, schema_descriptor):
        identified_problems = []
        
        check_null_allowed_res = self.check_null_allowed(
            field,
            value,
            schema_descriptor
        )
        if check_null_allowed_res is not None:
            identified_problems.append(check_null_allowed_res)
        else:
            if value is not None:
                try:
                    timestamp_value = int(value)
                except ValueError:
                    identified_problems.append(
                        {
                            "field": field,
                            "expected_timestamp": True,
                            "received_value": value
                        }
                    )
                    return False, identified_problems
                
                if "minTimestampValue" in schema_descriptor and timestamp_value < 0:
                    identified_problems.append(
                        {
                            "field": field,
                            "expected_min_timestamp": 0,
                            "received_value": timestamp_value
                        }
                    )
                
                if "maxTimestampValue" in schema_descriptor and timestamp_value > 253402300799:
                    identified_problems.append(
                        {
                            "field": field,
                            "expected_max_timestamp": 253402300799,
                            "received_value": timestamp_value
                        }
                    )
                
                if len(identified_problems) > 0:
                    return False, identified_problems
        
        return True, None
