const DATATYPE_OPTION_MAP = [
    {
        "type": "string",
        "constraints": [
            {
                "constraint_name": "null_allowed",
                "options": [true, false],
                "permissible_range": null
            },{
                "constraint_name": "min_length",
                "options": [true, false],
                "permissible_range": [0, "*"]
            },{
                "constraint_name": "max_length",
                "options": [true, false],
                "permissible_range": [1, "*"]
            }
        ]
    },{
        "type": "int",
        "constraints": [
            {
                "constraint_name": "null_allowed",
                "options": [true, false],
                "permissible_range": null
            },{
                "constraint_name": "min_value",
                "options": [true, false],
                "permissible_range": [-2147483648, 2147483647]
            },{
                "constraint_name": "max_value",
                "options": [true, false],
                "permissible_range": [-2147483648, 2147483647]
            }
        ]
    },{
        "type": "bigint",
        "constraints": [
            {
                "constraint_name": "null_allowed",
                "options": [true, false],
                "permissible_range": null
            },{
                "constraint_name": "min_value",
                "options": [true, false],
                "permissible_range": [-9223372036854775808, 9223372036854775807]
            },{
                "constraint_name": "max_value",
                "options": [true, false],
                "permissible_range": [-9223372036854775808, 9223372036854775807]
            }
        ]
    },{
        "type": "number",
        "constraints": [
            {
                "constraint_name": "null_allowed",
                "options": [true, false],
                "permissible_range": null
            },{
                "constraint_name": "min_value",
                "options": [true, false],
                "permissible_range": [-1.7976931348623157e+308, 1.7976931348623157e+308]
            },{
                "constraint_name": "max_value",
                "options": [true, false],
                "permissible_range": [-1.7976931348623157e+308, 1.7976931348623157e+308]
            }
        ]
    },{
        "type": "bool",
        "constraints": [
            {
                "constraint_name": "null_allowed",
                "options": [true, false],
                "permissible_range": null
            }
        ]
    },{
        "type": "email",
        "constraints": [
            {
                "constraint_name": "null_allowed",
                "options": [true, false],
            }
        ]
    },{
        "type": "timestamp",
        "constraints": [
            {
                "constraint_name": "null_allowed",
                "options": [true, false],
                "permissible_range": null
            }
        ]
    },{
        "type": "object",
        "constraints": [
            {
                "constraint_name": "null_allowed",
                "options": [true, false],
                "permissible_range": null
            }
        ]
    },{
        "type": "Array",
        "constraints": [
            {
                "constraint_name": "null_allowed",
                "options": [true, false],
                "permissible_range": null
            }
        ]
    },
]

export default DATATYPE_OPTION_MAP