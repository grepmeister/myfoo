#!/usr/bin/env python3

# is this the former argument thingy?

import json
from pprintpp import pprint as pp

from cmk.server_side_calls.v1 import SpecialAgentCommand, SpecialAgentConfig

def _agent_myfoo_parser(params):
    return params


def _agent_myfoo_arguments(params, _hostconfig):
    #pp(params)
    #pp(_hostconfig.macros)
    #print(help(_hostconfig))
    #pp(_hostconfig.ipv4_config)
    #pp(_hostconfig.ipv4_config.address)
    yield SpecialAgentCommand(
            command_arguments=[],
            #command_arguments=["my_command_arguments"],
            stdin=json.dumps(params["options"])
    )

# Defines a special agent
# https://cmk.jodok.tribe29.com/daily24/check_mk/plugin-api/cmk.server_side_calls/v1.html#cmk.server_side_calls.v1.SpecialAgentConfig
special_agent_myfoo = SpecialAgentConfig(
    # Special agent name. Has to match special agent executable name without the prefix agent_
    name="myfoo",
    # Translates the raw configured parameters into a validated data structure.
    # The result of the function will be passed as an argument to the command_function.
    # If you don’t want to parse your parameters, use the noop_parser.
    parameter_parser=_agent_myfoo_parser,
    commands_function=_agent_myfoo_arguments,
)
