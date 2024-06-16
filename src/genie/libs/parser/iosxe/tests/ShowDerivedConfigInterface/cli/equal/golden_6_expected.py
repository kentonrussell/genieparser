expected_output = {
    "derived_config":{
        "GigabitEthernet2/0/1":{
            "switchport_mode":"access",
            "switchport_block":"unicast",
            "switchport_port_security":{
                "maximum":{
                    "5":{

                    }
                },
                "aging_time":5,
                "aging_type":"inactivity",
                "switchport_port_security":True
            },
            "load_interval":60,
            "storm_control":{
                "broadcast_level_pps":"5k",
                "multicast_level_pps":"5k",
                "action":"trap"
            },
            "spanning_tree":{
                "portfast":True,
                "bpduguard":"enable"
            },
            "ip_dhcp_snooping_limit_rate":5
        }
    }
}