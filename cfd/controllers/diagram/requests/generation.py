def get_generation_request():
    return {
        "type": "object",
        "properties": {
            "data": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "column": {
                            "type": "string"
                        },
                        "values": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "x": {
                                        "type": "number"
                                    },
                                    "y": {
                                        "type": "number"
                                    }
                                },
                                "required": ["x", "y"]
                            }
                        },
                    },
                    "required": ["column"]
                }
            }
        },
        "required": ["data"]
    }