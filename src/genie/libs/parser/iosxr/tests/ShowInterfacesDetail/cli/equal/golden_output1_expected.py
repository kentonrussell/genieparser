expected_output = {
    "GigabitEthernet0/0/0/0": {
        "auto_negotiate": False,
        "bandwidth": 768,
        "carrier_delay": "10",
        "counters": {
            "carrier_transitions": 0,
            "in_abort": 0,
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_discards": 0,
            "in_frame": 0,
            "in_frame_errors": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_multicast_pkts": 0,
            "in_octets": 0,
            "in_overrun": 0,
            "in_parity": 0,
            "in_pkts": 0,
            "in_runts": 0,
            "in_throttles": 0,
            "in_unknown_protos": 0,
            "last_clear": "never",
            "out_applique": 0,
            "out_broadcast_pkts": 0,
            "out_buffer_failures": 0,
            "out_buffer_swapped_out": 0,
            "out_discards": 0,
            "out_errors": 0,
            "out_multicast_pkts": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "out_resets": 0,
            "out_underruns": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 30,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "description": "desc",
        "duplex_mode": "full",
        "enabled": False,
        "encapsulations": {"encapsulation": "arpa"},
        "flow_control": {"flow_control_receive": False, "flow_control_send": False},
        "interface_state": 0,
        "ipv4": {"10.1.1.1/24": {"ip": "10.1.1.1", "prefix_length": "24"}},
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "administratively down",
        "oper_status": "down",
        "location": "unknown",
        "mac_address": "aaaa.bbff.8888",
        "mtu": 1600,
        "phys_address": "5254.00ff.0c7e",
        "port_speed": "1000Mb/s",
        "reliability": "255/255",
        "rxload": "0/255",
        "txload": "0/255",
        "types": "gigabitethernet",
    },
    "GigabitEthernet0/0/0/0.10": {
        "bandwidth": 768,
        "counters": {
            "in_broadcast_pkts": 0,
            "in_discards": 0,
            "in_multicast_pkts": 0,
            "in_octets": 0,
            "in_pkts": 0,
            "in_unknown_protos": 0,
            "last_clear": "never",
            "out_broadcast_pkts": 0,
            "out_discards": 0,
            "out_multicast_pkts": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "enabled": False,
        "encapsulations": {
            "encapsulation": "802.1q " "virtual " "lan",
            "first_dot1q": "10",
            "second_dot1q": "10",
        },
        "interface_state": 0,
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "administratively down",
        "oper_status": "down",
        "mac_address": "aaaa.bbff.8888",
        "mtu": 1608,
        "reliability": "255/255",
        "rxload": "0/255",
        "txload": "0/255",
        "types": "vlan sub-(s)",
    },
    "GigabitEthernet0/0/0/0.20": {
        "bandwidth": 768,
        "counters": {
            "in_broadcast_pkts": 0,
            "in_discards": 0,
            "in_multicast_pkts": 0,
            "in_octets": 0,
            "in_pkts": 0,
            "in_unknown_protos": 0,
            "last_clear": "never",
            "out_broadcast_pkts": 0,
            "out_discards": 0,
            "out_multicast_pkts": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "enabled": False,
        "encapsulations": {
            "encapsulation": "802.1q " "virtual " "lan",
            "first_dot1q": "20",
        },
        "interface_state": 0,
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "administratively down",
        "oper_status": "down",
        "mac_address": "aaaa.bbff.8888",
        "mtu": 1604,
        "reliability": "255/255",
        "rxload": "0/255",
        "txload": "0/255",
        "types": "vlan sub-(s)",
    },
    "GigabitEthernet0/0/0/1": {
        "arp_timeout": "04:00:00",
        "arp_type": "arpa",
        "auto_negotiate": False,
        "bandwidth": 1000000,
        "carrier_delay": "10",
        "counters": {
            "carrier_transitions": 1,
            "in_abort": 0,
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_discards": 0,
            "in_frame": 0,
            "in_frame_errors": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_multicast_pkts": 29056,
            "in_octets": 18221418,
            "in_overrun": 0,
            "in_parity": 0,
            "in_pkts": 146164,
            "in_runts": 0,
            "in_throttles": 0,
            "in_unknown_protos": 0,
            "last_clear": "never",
            "out_applique": 0,
            "out_broadcast_pkts": 2,
            "out_buffer_failures": 0,
            "out_buffer_swapped_out": 0,
            "out_discards": 0,
            "out_errors": 0,
            "out_multicast_pkts": 6246,
            "out_octets": 10777610,
            "out_pkts": 123696,
            "out_resets": 0,
            "out_underruns": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "duplex_mode": "full",
        "enabled": True,
        "encapsulations": {"encapsulation": "arpa"},
        "flow_control": {"flow_control_receive": False, "flow_control_send": False},
        "interface_state": 1,
        "ipv4": {"10.1.5.1/24": {"ip": "10.1.5.1", "prefix_length": "24"}},
        "last_input": "00:01:09",
        "last_link_flapped": "1w5d",
        "last_output": "00:01:09",
        "line_protocol": "up",
        "oper_status": "up",
        "location": "unknown",
        "mac_address": "5254.00ff.6459",
        "mtu": 1514,
        "phys_address": "5254.00ff.6459",
        "port_speed": "1000Mb/s",
        "reliability": "255/255",
        "rxload": "0/255",
        "txload": "0/255",
        "types": "gigabitethernet",
    },
    "MgmtEth0/0/CPU0/0": {
        "auto_negotiate": True,
        "bandwidth": 0,
        "carrier_delay": "10",
        "counters": {
            "carrier_transitions": 0,
            "in_abort": 0,
            "in_broadcast_pkts": 0,
            "in_crc_errors": 0,
            "in_discards": 0,
            "in_frame": 0,
            "in_frame_errors": 0,
            "in_giants": 0,
            "in_ignored": 0,
            "in_multicast_pkts": 0,
            "in_octets": 0,
            "in_overrun": 0,
            "in_parity": 0,
            "in_pkts": 0,
            "in_runts": 0,
            "in_throttles": 0,
            "in_unknown_protos": 0,
            "last_clear": "never",
            "out_applique": 0,
            "out_broadcast_pkts": 0,
            "out_buffer_failures": 0,
            "out_buffer_swapped_out": 0,
            "out_discards": 0,
            "out_errors": 0,
            "out_multicast_pkts": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "out_resets": 0,
            "out_underruns": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "duplex_mode": "duplex unknown",
        "enabled": False,
        "encapsulations": {"encapsulation": "arpa"},
        "flow_control": {"flow_control_receive": False, "flow_control_send": False},
        "interface_state": 0,
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "administratively down",
        "oper_status": "down",
        "location": "unknown",
        "mac_address": "5254.00ff.3007",
        "mtu": 1514,
        "phys_address": "5254.00ff.3007",
        "port_speed": "0",
        "reliability": "255/255",
        "rxload": "unknown",
        "txload": "unknown",
        "types": "management ethernet",
    },
    "Loopback0": {
        "bandwidth": 0,
        "description": "loopback0 BGP test",
        "enabled": True,
        "encapsulations": {"encapsulation": "loopback"},
        "interface_state": 1,
        "ipv4": {"10.255.20.81/32": {"ip": "10.255.20.81", "prefix_length": "32"}},
        "last_input": "Unknown",
        "last_link_flapped": "13:45:11",
        "last_output": "Unknown",
        "line_protocol": "up",
        "mtu": 1500,
        "oper_status": "up",
        "reliability": "Unknown",
        "rxload": "unknown",
        "txload": "unknown",
    },
    "Null0": {
        "bandwidth": 0,
        "counters": {
            "in_broadcast_pkts": 0,
            "in_discards": 0,
            "in_multicast_pkts": 0,
            "in_octets": 0,
            "in_pkts": 0,
            "in_unknown_protos": 0,
            "last_clear": "never",
            "out_broadcast_pkts": 0,
            "out_discards": 0,
            "out_multicast_pkts": 0,
            "out_octets": 0,
            "out_pkts": 0,
            "rate": {
                "in_rate": 0,
                "in_rate_pkts": 0,
                "load_interval": 300,
                "out_rate": 0,
                "out_rate_pkts": 0,
            },
        },
        "enabled": True,
        "encapsulations": {"encapsulation": "null"},
        "last_input": "never",
        "last_output": "never",
        "line_protocol": "up",
        "oper_status": "up",
        "mtu": 1500,
        "reliability": "255/255",
        "rxload": "unknown",
        "txload": "unknown",
        "types": "null",
    },
}
