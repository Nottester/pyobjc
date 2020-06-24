# This file is generated by objective.metadata
#
# Last update: Thu Jun 25 00:11:24 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
misc.update(
    {
        "timespec": objc.createStructType(
            "timespec", b"{timespec=ll}", ["tv_sec", "tv_nsec"]
        )
    }
)
constants = """$$"""
enums = """$DISPATCH_AUTORELEASE_FREQUENCY_INHERIT@0$DISPATCH_AUTORELEASE_FREQUENCY_NEVER@2$DISPATCH_AUTORELEASE_FREQUENCY_WORK_ITEM@1$DISPATCH_BLOCK_ASSIGN_CURRENT@4$DISPATCH_BLOCK_BARRIER@1$DISPATCH_BLOCK_DETACHED@2$DISPATCH_BLOCK_ENFORCE_QOS_CLASS@32$DISPATCH_BLOCK_INHERIT_QOS_CLASS@16$DISPATCH_BLOCK_NO_QOS_CLASS@8$DISPATCH_IO_RANDOM@1$DISPATCH_IO_STOP@1$DISPATCH_IO_STREAM@0$DISPATCH_IO_STRICT_INTERVAL@1$DISPATCH_MACH_SEND_DEAD@1$DISPATCH_MEMORYPRESSURE_CRITICAL@4$DISPATCH_MEMORYPRESSURE_NORMAL@1$DISPATCH_MEMORYPRESSURE_WARN@2$DISPATCH_PROC_EXEC@536870912$DISPATCH_PROC_EXIT@2147483648$DISPATCH_PROC_FORK@1073741824$DISPATCH_PROC_SIGNAL@134217728$DISPATCH_QUEUE_PRIORITY_BACKGROUND@-32768$DISPATCH_QUEUE_PRIORITY_DEFAULT@0$DISPATCH_QUEUE_PRIORITY_HIGH@2$DISPATCH_QUEUE_PRIORITY_LOW@-2$DISPATCH_TIMER_STRICT@1$DISPATCH_TIME_FOREVER@18446744073709551615$DISPATCH_TIME_NOW@0$DISPATCH_VNODE_ATTRIB@8$DISPATCH_VNODE_DELETE@1$DISPATCH_VNODE_EXTEND@4$DISPATCH_VNODE_FUNLOCK@256$DISPATCH_VNODE_LINK@16$DISPATCH_VNODE_RENAME@32$DISPATCH_VNODE_REVOKE@64$DISPATCH_VNODE_WRITE@2$NSEC_PER_MSEC@1000000$NSEC_PER_SEC@1000000000$NSEC_PER_USEC@1000$USEC_PER_SEC@1000000$"""
misc.update({})
functions = {
    "dispatch_io_create_with_io": (
        b"@L@@@?",
        "",
        {
            "retval": {"already_retained": True},
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}, 1: {"type": "i"}},
                    }
                }
            },
        },
    ),
    "dispatch_source_get_data": (b"L@",),
    "dispatch_data_create_concat": (b"@@@", "", {"retval": {"already_retained": True}}),
    "dispatch_semaphore_create": (b"@l", "", {"retval": {"already_retained": True}}),
    "dispatch_activate": (b"v@",),
    "dispatch_io_set_interval": (b"v@QL",),
    "dispatch_assert_queue_not": (b"v@", "", {"comment": "XXX: V2 API"}),
    "dispatch_barrier_async": (
        b"v@@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_after": (
        b"vQ@@?",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_io_get_descriptor": (b"i@",),
    "dispatch_source_set_timer": (b"v@QQQ",),
    "dispatch_get_current_queue": (b"@",),
    "dispatch_io_close": (b"v@L",),
    "dispatch_source_get_mask": (b"L@",),
    "dispatch_queue_attr_make_initially_inactive": (b"@@",),
    "dispatch_block_create": (
        b"@?L@?",
        "",
        {
            "retval": {
                "callable": {"retval": {"type": "v"}, "arguments": {0: {"type": "^v"}}},
                "already_retained": True,
            },
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            },
        },
    ),
    "dispatch_block_perform": (
        b"vL@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_block_testcancel": (
        b"l@?",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_group_async": (
        b"v@@@?",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_read": (
        b"viL@@?",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"comment": "dispatch_data_t", "type": "@"},
                            2: {"type": "i"},
                        },
                    }
                }
            }
        },
    ),
    "dispatch_assert_queue_barrier": (b"v@",),
    "dispatch_once": (
        b"vN^l@?",
        "",
        {
            "arguments": {
                0: {"c_array_of_fixed_length": 1},
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                },
            }
        },
    ),
    "dispatch_source_set_registration_handler": (
        b"v@@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_once_f": (
        b"vN^l^v^?",
        "",
        {
            "arguments": {
                0: {"c_array_of_fixed_length": 1},
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    },
                    "callable_retained": False,
                },
            }
        },
    ),
    "dispatch_get_context": (b"^v@",),
    "dispatch_set_target_queue": (b"v@@",),
    "dispatch_data_copy_region": (
        b"@@Lo^L",
        "",
        {"retval": {"already_retained": True}},
    ),
    "dispatch_notify": (
        b"v@?@@?",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                },
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                },
            }
        },
    ),
    "dispatch_queue_set_specific": (
        b"v@^v^v^?",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    },
                    "callable_retained": True,
                }
            }
        },
    ),
    "dispatch_io_write": (
        b"v@q@@@?",
        "",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "B"},
                            2: {"type": "@"},
                            3: {"type": "i"},
                        },
                    }
                }
            }
        },
    ),
    "dispatch_barrier_async_f": (
        b"v@^v^?",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    },
                    "callable_retained": True,
                }
            }
        },
    ),
    "dispatch_block_cancel": (
        b"v@?",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_group_async_f": (
        b"v@@^v^?",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_apply_f": (
        b"vL@^v^?",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}, 1: {"type": "L"}},
                    }
                }
            }
        },
    ),
    "dispatch_set_context": (b"v@^v",),
    "dispatch_queue_attr_make_with_qos_class": (b"@@Ii",),
    "dispatch_suspend": (b"v@",),
    "dispatch_set_finalizer_f": (
        b"v@^?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    },
                    "callable_retained": True,
                }
            }
        },
    ),
    "dispatch_sync": (
        b"v@@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_block_notify": (
        b"v@?@@?",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                },
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                },
            }
        },
    ),
    "dispatch_queue_create": (
        b"@^t@",
        "",
        {"arguments": {0: {"c_array_delimited_by_null": True, "type_modifier": "n"}}},
    ),
    "dispatch_group_wait": (b"l@Q",),
    "dispatch_main": (b"v",),
    "dispatch_barrier_sync": (
        b"v@@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_source_set_cancel_handler_f": (
        b"v@^?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    },
                    "callable_retained": True,
                }
            }
        },
    ),
    "dispatch_group_create": (b"@", "", {"retval": {"already_retained": True}}),
    "dispatch_source_set_event_handler_f": (
        b"v@^?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    },
                    "callable_retained": True,
                }
            }
        },
    ),
    "dispatch_queue_get_specific": (b"^v@^v",),
    "dispatch_async_f": (
        b"v@^v^?",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    },
                    "callable_retained": True,
                }
            }
        },
    ),
    "dispatch_source_set_event_handler": (
        b"v@@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_time": (b"QQq",),
    "dispatch_queue_get_label": (
        b"^t@",
        "",
        {"retval": {"c_array_delimited_by_null": True}},
    ),
    "dispatch_source_cancel": (b"v@",),
    "dispatch_group_enter": (b"v@",),
    "dispatch_io_create_with_path": (
        b"@L^tiS@@?",
        "",
        {
            "retval": {"already_retained": True},
            "arguments": {
                1: {"c_array_delimited_by_null": True, "type_modifier": "n"},
                5: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}, 1: {"type": "i"}},
                    }
                },
            },
        },
    ),
    "dispatch_testcancel": (b"l@",),
    "dispatch_io_read": (
        b"v@qL@@?",
        "",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "B"},
                            2: {"type": "@"},
                            3: {"type": "i"},
                        },
                    }
                }
            }
        },
    ),
    "dispatch_source_testcancel": (b"l@",),
    "dispatch_source_set_registration_handler_f": (
        b"v@^?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    },
                    "callable_retained": True,
                }
            }
        },
    ),
    "dispatch_barrier_sync_f": (
        b"v@^v^?",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    },
                    "callable_retained": False,
                }
            }
        },
    ),
    "dispatch_group_notify_f": (
        b"v@@^v^?",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_data_create_subrange": (
        b"@@LL",
        "",
        {"retval": {"already_retained": True}},
    ),
    "dispatch_semaphore_signal": (b"l@",),
    "dispatch_cancel": (b"v@",),
    "dispatch_queue_get_qos_class": (
        b"I@^i",
        "",
        {"arguments": {1: {"type_modifier": "o"}}},
    ),
    "dispatch_sync_f": (
        b"v@^v^?",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    },
                    "callable_retained": False,
                }
            }
        },
    ),
    "dispatch_get_main_queue": (b"@",),
    "dispatch_data_apply": (
        b"B@@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"B"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "@"},
                            2: {"type": "L"},
                            3: {"type": "n^v", "c_array_length_in_arg": 4},
                            4: {"type": "L"},
                        },
                    }
                }
            }
        },
    ),
    "dispatch_write": (
        b"vi@@@?",
        "",
        {
            "arguments": {
                1: {"comment": "dispatch_data_t"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"comment": "dispatch_data_t", "type": "@"},
                            2: {"type": "i"},
                        },
                    }
                },
            }
        },
    ),
    "dispatch_io_barrier": (
        b"v@@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_get_global_queue": (b"@lL",),
    "dispatch_walltime": (b"Qn^{timespec=ll}q",),
    "dispatch_assert_queue": (b"v@",),
    "dispatch_get_specific": (b"^v^v",),
    "dispatch_after_f": (
        b"vQ@^v^?",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    },
                    "callable_retained": True,
                }
            }
        },
    ),
    "dispatch_source_merge_data": (b"v@L",),
    "dispatch_resume": (b"v@",),
    "dispatch_semaphore_wait": (b"l@Q",),
    "dispatch_io_create": (
        b"@Li@@?",
        "",
        {
            "retval": {"already_retained": True},
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}, 1: {"type": "i"}},
                    }
                }
            },
        },
    ),
    "dispatch_source_create": (
        b"@^{dispatch_source_type_s=}LL@",
        "",
        {"retval": {"already_retained": True}},
    ),
    "dispatch_wait": (b"l@Q",),
    "dispatch_io_set_high_water": (b"v@L",),
    "dispatch_data_create_map": (
        b"@@o^^vo^L",
        "",
        {"retval": {"already_retained": True}},
    ),
    "dispatch_async": (
        b"v@@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_group_notify": (
        b"v@@@?",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_block_create_with_qos_class": (
        b"@?LIi@?",
        "",
        {
            "retval": {
                "callable": {"retval": {"type": "v"}, "arguments": {0: {"type": "^v"}}},
                "already_retained": True,
            },
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            },
        },
    ),
    "dispatch_io_set_low_water": (b"v@L",),
    "dispatch_data_get_size": (b"L@",),
    "dispatch_block_wait": (
        b"l@?Q",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_group_leave": (b"v@",),
    "dispatch_source_get_handle": (b"L@",),
    "dispatch_apply": (
        b"vL@@?",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}, 1: {"type": "L"}},
                    }
                }
            }
        },
    ),
    "dispatch_data_create": (
        b"@^vL@@?",
        "",
        {
            "retval": {"already_retained": True},
            "arguments": {
                0: {"type_modifier": "n", "c_array_length_in_arg": 1},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                },
            },
        },
    ),
    "dispatch_queue_attr_make_with_autorelease_frequency": (b"@@L",),
    "dispatch_source_set_cancel_handler": (
        b"v@@?",
        "",
        {
            "arguments": {
                1: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": "^v"}},
                    }
                }
            }
        },
    ),
    "dispatch_queue_create_with_target": (
        b"@^t@@",
        "",
        {
            "comment": "XXX: V2 API",
            "arguments": {0: {"c_array_delimited_by_null": True, "type_modifier": "n"}},
        },
    ),
}
misc.update(
    {
        "dispatch_source_t": objc.createOpaquePointerType(
            "dispatch_source_t", b"^{dispatch_source_type_s=}"
        )
    }
)
expressions = {
    "DISPATCH_CURRENT_QUEUE_LABEL": "None",
    "DISPATCH_QUEUE_SERIAL": "None",
    "DISPATCH_QUEUE_SERIAL_WITH_AUTORELEASE_POOL": "dispatch_queue_attr_make_with_autorelease_frequency(DISPATCH_QUEUE_SERIAL, DISPATCH_AUTORELEASE_FREQUENCY_WORK_ITEM)",
    "DISPATCH_APPLY_AUTO": "None",
    "DISPATCH_QUEUE_SERIAL_INACTIVE": "dispatch_queue_attr_make_initially_inactive(DISPATCH_QUEUE_SERIAL)",
    "DISPATCH_DATA_DESTRUCTOR_DEFAULT": "None",
    "DISPATCH_QUEUE_CONCURRENT_INACTIVE": "dispatch_queue_attr_make_initially_inactive(DISPATCH_QUEUE_CONCURRENT)",
    "DISPATCH_QUEUE_CONCURRENT_WITH_AUTORELEASE_POOL": "dispatch_queue_attr_make_with_autorelease_frequency(DISPATCH_QUEUE_CONCURRENT, DISPATCH_AUTORELEASE_FREQUENCY_WORK_ITEM)",
    "DISPATCH_TARGET_QUEUE_DEFAULT": "None",
}

# END OF FILE
