#!/usr/bin/env python3

from cmk.rulesets.v1 import Help, Label, Title

from cmk.rulesets.v1.form_specs import (
    DictElement,
    DictGroup,
    Dictionary,
    InputHint,
    List,
    String,
    validators,
)
from cmk.rulesets.v1.rule_specs import SpecialAgent, Topic

# to log to ~/var/log/web.log
import logging

def _parameter_form() -> Dictionary:

    logger.info("INFO: myfoo ruleset message")

    return Dictionary(
        title=Title("myfoo Aggregations"),
        elements={
            "options": DictElement(
                required=True,
                parameter_form=List(
                    element_template=Dictionary(
                        elements={
                            "url": DictElement(
                                parameter_form=String(
                                    title=Title("URL"),
                                    field_size=200,
                                    help_text=Help(
                                        "The URL to monitor. This URL must include the protocol (HTTP or "
                                        "HTTPS), the full address and, if needed, also the port of the endpoint "
                                        "if using a non standard port. The URL may also include query "
                                        "parameters or anchors. You may use macros in this field. The most "
                                        "common ones are $HOSTNAME$, $HOSTALIAS$ or $HOSTADDRESS$. "
                                    ),
                                    prefill=InputHint(
                                        "https://$HOSTNAME$:port/path/to/resource"
                                    ),
                                    custom_validate=(
                                        validators.Url(
                                            [
                                                validators.UrlProtocol.HTTP,
                                                validators.UrlProtocol.HTTPS,
                                            ],
                                        ),
                                    ),
                                    # macro_support=True, # deactivated to avoid conflicts with manual help_text
                                ),
                                required=True,
                            ),
                            "add_headers": DictElement(
                                parameter_form=List(
                                    title=Title("Additional header lines"),
                                    help_text=Help(
                                        "These additional header lines will be used in the request. You may use "
                                        "any header lines that follow the conventions for header entries. Please "
                                        "note that you don't need a colon to separate key and value as you have "
                                        "a dedicated input field for each."
                                    ),
                                    element_template=Dictionary(elements=header_dict_elements),
                                ),
                            ),
                        },
                    ),
                    help_text=Help(
                        "This rule allows you to check multiple "
                    ),
                ),
            )
        },
    )

header_dict_elements = {
    "header_name": DictElement(
        group=DictGroup(),
        parameter_form=String(label=Label("Name"), prefill=InputHint("Authorization")),
        required=True,
    ),
    "header_value": DictElement(
        group=DictGroup(),
        parameter_form=String(label=Label("Value"), prefill=InputHint("Bearer C0FFEEBEEF")),
        required=True,
    ),
}


rule_spec_myfoo_special_agent = SpecialAgent(
    name="myfoo",
    title=Title("myfoo Special Agent"),
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_form,
)
