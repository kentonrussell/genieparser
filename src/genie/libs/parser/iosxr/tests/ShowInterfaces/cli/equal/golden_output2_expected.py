expected_output = {
    "Bundle-Ether1": {
        "enabled": True,
        "line_protocol": "up",
        "oper_status": "up",
        "interface_state_transitions": 9,
        "type": "Aggregated Ethernet interface(s)",
        "mac_address": "00bc.60ff.1119",
        "description": "to-ML26-BE1",
        "ipv4": {"192.168.0.25/30": {"ip": "192.168.0.25", "prefix_length": "30"}},
        "mtu": 1514,
        "bandwidth": 100000000,
        "bandwidth_max": 100000000,
        "reliability": "255/255",
        "txload": "0/255",
        "rxload": "0/255",
        "encapsulations": {"encapsulation": "arpa"},
        "duplex_mode": "full",
        "port_speed": "100000Mb/s",
        "loopback": "not set",
        "last_link_flapped": "3w3d",
        "arp_type": "arpa",
        "arp_timeout": "04:00:00",
        "port_channel": {
            "member_count": 1,
            "members": {
                "HundredGigE0/0/1/2/0": {
                    "interface": "HundredGigE0/0/1/2/0",
                    "duplex_mode": "Full-duplex",
                    "speed": "100000Mb/s",
                    "state": "Active",
                }
            },
        },
        "last_input": "00:00:00",
        "last_output": "00:00:00",
        "counters": {
            "last_clear": "never",
            "rate": {
                "load_interval": 30,
                "in_rate": 1000,
                "in_rate_pkts": 0,
                "out_rate": 2000,
                "out_rate_pkts": 1,
            },
            "in_pkts": 1716386544,
            "in_octets": 751342403591,
            "in_total_drops": 0,
            "in_unknown_protos": 0,
            "in_broadcast_pkts": 6,
            "in_multicast_pkts": 642898,
            "in_runts": 0,
            "in_giants": 0,
            "in_throttles": 0,
            "in_parity": 0,
            "in_errors": 0,
            "in_crc_errors": 0,
            "in_frame": 0,
            "in_overrun": 0,
            "in_ignored": 0,
            "in_abort": 0,
            "out_pkts": 1714349214,
            "out_octets": 754526715390,
            "out_total_drops": 0,
            "out_broadcast_pkts": 12,
            "out_multicast_pkts": 642896,
            "out_errors": 0,
            "out_underruns": 0,
            "out_applique": 0,
            "out_resets": 0,
            "out_buffer_failure": 0,
            "out_buffers_swapped": 0,
            "carrier_transitions": 0,
        },
    }
}
