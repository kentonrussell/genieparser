expected_output = {
  'primary_load_time_percent': 1,
  'secondary_load_time_percent': 0,
  'one_minute_load_percent': 1,
  'five_minute_load_percent': 0,
  'ntp_time': '11:04:51.711 PDT Fri Sep 1 2023',
  'smart_licensing_status': {
      'export_authorization_key': {
          'features_authorized': 'none'},
      'utility': {
          'status': 'DISABLED'},
      'smart_licensing_using_policy': {
          'status': 'ENABLED'},
      'data_privacy': {
          'sending_hostname': 'yes',
          'callhome_hostname_privacy': 'DISABLED',
          'smart_licensing_hostname_privacy': 'DISABLED',
          'version_privacy': 'DISABLED'},
      'transport': {
          'type': 'Smart',
          'url': 'https://smartreceiver.cisco.com/licservice/license',
          'proxy': {
              'address': '173.36.224.108',
              'port': 80,
              'username': '<empty>',
              'password': '<empty>'},
          'server_identity_check': 'True'},
      'miscellaneous': {
          'custom_id': '<empty>'},
      'policy': {
          'policy_in_use': 'Installed On Aug 30 18:45:53 2023 PDT',
          'policy_name': 'SLE Policy',
          'reporting_ack_required': 'yes (Customer Policy)',
          'unenforced_non_export_perpetual_attributes': {
              'first_report_requirement_days': '30 (Customer Policy)',
              'reporting_frequency_days': '60 (Customer Policy)',
              'report_on_change_days': '60 (Customer Policy)'},
          'unenforced_non_export_subscription_attributes': {
              'first_report_requirement_days': '120 (Customer Policy)',
              'reporting_frequency_days': '111 (Customer Policy)',
              'report_on_change_days': '111 (Customer Policy)'},
          'enforced_perpetual_subscription_license_attributes': {
              'first_report_requirement_days': '0 (CISCO default)',
              'reporting_frequency_days': '90 (Customer Policy)',
              'report_on_change_days': '60 (Customer Policy)'},
          'export_perpetual_subscription_license_attributes': {
              'first_report_requirement_days': '0 (CISCO default)',
              'reporting_frequency_days': '30 (Customer Policy)',
              'report_on_change_days': '30 (Customer Policy)'}},
      'usage_reporting': {
          'last_ack_received': 'Aug 30 19:03:00 2023 PDT',
          'next_ack_deadline': 'Oct 29 19:03:00 2023 PDT',
          'reporting_push_interval': '30  days State(4) InPolicy(60)',
          'next_ack_push_check': 'Aug 30 19:06:59 2023 PDT',
          'next_report_push': 'Aug 30 21:04:57 2023 PDT',
          'last_report_push': 'Aug 30 20:57:57 2023 PDT',
          'last_report_file_write': '<none>'}},
 'license_usage': {
     'handle': {
          1: {
              'license': 'network-advantage',
              'entitlement_tag': 'regid.2017-05.com.cisco.advantagek9-C9400,1.0_61a546cd-1037-47cb-bbe6-7cad3217a7b3',
              'description': 'C9400 Network Advantage',
              'count': 2,
              'version': '1.0',
              'status': 'IN USE(15)',
              'status_time': 'Aug 30 21:02:35 2023 PDT',
              'request_time': 'Aug 30 21:03:11 2023 PDT',
              'export_status': 'NOT RESTRICTED',
              'feature_name': 'network-advantage',
              'feature_description': 'C9400 Network Advantage',
              'enforcement_type': 'NOT ENFORCED',
              'license_type': 'Perpetual',
              'measurements': {
                  'entitlement': {
                      'interval': '00:15:00',
                      'current_value': 2}},
              'soft_enforced': 'True'},
          2: {'license': 'dna-advantage',
              'entitlement_tag': 'regid.2017-05.com.cisco.dna_advantage-C9400,1.0_6e77dbc1-0da3-466c-8414-97c8ee4d48ce',
              'description': 'C9400 DNA Advantage',
              'count': 1,
              'version': '1.0',
              'status': 'IN USE(15)',
              'status_time': 'Aug 30 21:02:35 2023 PDT',
              'request_time': 'Aug 30 21:02:35 2023 PDT',
              'export_status': 'NOT RESTRICTED',
              'feature_name': 'dna-advantage',
              'feature_description': 'C9400 DNA Advantage',
              'enforcement_type': 'NOT ENFORCED',
              'license_type': 'Subscription',
              'measurements': {
                  'entitlement': {
                      'interval': '00:15:00',
                      'current_value': 1}},
              'soft_enforced': 'True'}}},
 'product_information': {
    'udi': {
         'pid': 'C9407R', 'sn': 'FXS2119Q2U7'},
    'ha_udi_list': {
        'active': {
            'pid': 'C9407R', 'sn': 'FXS2119Q2U7'},
        'standby': {
            'pid': 'C9407R', 'sn': 'FXS2119Q2U7'}}},
 'agent_version': {
     'smart_agent_for_licensing': '5.1.31_rel/142'},
 'upcoming_scheduled_jobs': {
    'current_time': 'Sep 01 11:04:51 2023 PDT',
    'daily': 'Sep 01 21:02:38 2023 PDT (9 hours, 57 minutes, 47 seconds remaining)',
    'authorization_renewal': 'Expired Not Rescheduled',
    'init_flag_check': 'Expired Not Rescheduled',
    'reservation_configuration_mismatch_between_nodes_in_ha_mode': 'Expired Not Rescheduled',
    'start_utility_measurements': 'Sep 01 11:12:39 2023 PDT (7 minutes, 48 seconds remaining)',
    'send_utility_rum_reports': 'Expired Not Rescheduled',
    'save_unreported_rum_reports': 'Sep 01 11:57:49 2023 PDT (52 minutes, 58 seconds remaining)',
    'process_utility_rum_reports': 'Sep 01 21:04:25 2023 PDT (9 hours, 59 minutes, 34 seconds remaining)',
    'data_synchronization': 'Expired Not Rescheduled',
    'external_event': 'Oct 29 18:41:26 2023 PDT (58 days, 7 hours, 36 minutes, 35 seconds remaining)',
    'operational_model': 'Expired Not Rescheduled'},
 'communication_statistics': {
    'communication_level_allowed': 'DIRECT',
    'overall_state': '<empty>',
    'trust_establishment': {
        'attempts': 'Total=0, Success=0, Fail=0',
        'ongoing_failure': 'Overall=0 Communication=0',
        'last_response': '<none>',
        'failure_reason': '<none>',
        'last_success_time': '<none>',
        'last_failure_time': '<none>'},
    'trust_acknowledgement': {
        'attempts': 'Total=0, Success=0, Fail=0',
        'ongoing_failure': 'Overall=0 Communication=0',
        'last_response': '<none>',
        'failure_reason': '<none>',
        'last_success_time': '<none>',
        'last_failure_time': '<none>'},
    'usage_reporting': {
        'attempts': 'Total=2, Success=0, Fail=2',
        'ongoing_failure': 'Overall=2 Communication=0',
        'last_response': 'INVALID STATUS CODE on Aug 30 23:12:38 2023 PDT',
        'failure_reason': '{"product_instance_identifier":["The identity for the instance f654477d-627f-4049-bada-b44f18612bcc is not valid.Please re-register the instance."]}',
        'last_success_time': '<none>',
        'last_failure_time': 'Aug 30 23:12:38 2023 PDT'},
    'result_polling': {
        'attempts': 'Total=0, Success=0, Fail=0',
        'ongoing_failure': 'Overall=0 Communication=0',
        'last_response': '<none>',
        'failure_reason': '<none>',
        'last_success_time': '<none>',
        'last_failure_time': '<none>'},
    'authorization_request': {
        'attempts': 'Total=0, Success=0, Fail=0',
        'ongoing_failure': 'Overall=0 Communication=0',
        'last_response': '<none>',
        'failure_reason': '<none>',
        'last_success_time': '<none>',
        'last_failure_time': '<none>'},
    'authorization_confirmation': {
        'attempts': 'Total=0, Success=0, Fail=0',
        'ongoing_failure': 'Overall=0 Communication=0',
        'last_response': '<none>',
        'failure_reason': '<none>',
        'last_success_time': '<none>',
        'last_failure_time': '<none>'},
    'authorization_return': {
        'attempts': 'Total=0, Success=0, Fail=0',
        'ongoing_failure': 'Overall=0 Communication=0',
        'last_response': '<none>',
        'failure_reason': '<none>',
        'last_success_time': '<none>',
        'last_failure_time': '<none>'},
    'trust_sync': {
        'attempts': 'Total=2, Success=0, Fail=2',
        'ongoing_failure': 'Overall=2 Communication=0',
        'last_response': 'INVALID STATUS CODE on Aug 30 23:12:28 2023 PDT',
        'failure_reason': '{"product_instance_identifier":["The identity for the instance f654477d-627f-4049-bada-b44f18612bcc is not valid.Please re-register the instance."]}',
        'last_success_time': '<none>',
        'last_failure_time': 'Aug 30 23:12:28 2023 PDT'},
        'hello_message': {'attempts': 'Total=0, Success=0, Fail=0',
        'ongoing_failure': 'Overall=0 Communication=0',
        'last_response': '<none>',
        'failure_reason': '<none>',
        'last_success_time': '<none>',
        'last_failure_time': '<none>'}},
 'license_certificates': {
     'production_cert': 'True'},
 'ha_info': {
     'rp_role': 'Active',
    'chassis_role': 'Active',
    'behavior_role': 'Active',
    'rmf': 'True',
    'cf': 'True',
    'cf_state': 'Stateless',
    'message_flow_allowed': 'False'},
 'reservation_info': {
    'license_reservation': 'DISABLED',
    'overall_status': {
        'active': {
            'pid': 'C9407R',
            'sn': 'FXS2119Q2U7',
            'reservation_status': 'NOT INSTALLED',
            'request_code': '<none>',
            'last_return_code': '<none>',
            'last_confirmation_code': '<none>',
            'reservation_authorization_code': '<none>'},
        'standby': {
            'pid': 'C9407R',
            'sn': 'FXS2119Q2U7',
            'reservation_status': 'NOT INSTALLED',
            'request_code': '<none>',
            'last_return_code': '<none>',
            'last_confirmation_code': '<none>',
            'reservation_authorization_code': '<none>'}},
    'purchased_licenses': 'No Purchase Information Available'},
  'other_info': {
      'software_id': 'regid.2017-05.com.cisco.C9400,v1_ad928212-d182-407e-ac85-29e213602efa',
      'agent_state': 'authorized',
      'ts_enable': 'True',
      'transport': 'Smart',
      'default_url': 'https://smartreceiver.cisco.com/licservice/license',
      'locale': 'en_US.UTF-8',
      'debug_flags': '0x7',
      'privacy_send_hostname': 'True',
      'privacy_send_ip': 'True',
      'build_type': 'Production',
      'sizeof_char': 1,
      'sizeof_int': 4,
      'sizeof_long': 4,
      'sizeof_char_*': 8,
      'sizeof_time_t': 4,
      'sizeof_size_t': 8,
      'endian': 'Big',
      'write_erase_occurred': 'False',
      'xos_version': '0.12.0.0',
      'config_persist_received': 'False',
      'message_version': '1.3',
      'connect_info_name': '<empty>',
      'connect_info_version': '<empty>',
      'connect_info_additional': '<empty>',
      'connect_info_prod': 'False',
      'connect_info_capabilities': '<empty>',
      'agent_capabilities': 'UTILITY, DLC, AppHA, MULTITIER, EXPORT_2, OK_TRY_AGAIN, POLICY_USAGE',
      'check_point_interface': 'True',
      'config_management_interface': 'False',
      'license_map_interface': 'True',
      'ha_interface': 'True',
      'trusted_store_interface': 'True',
      'platform_data_interface': 'True',
      'crypto_version_2_interface': 'False',
      'sapluginmgmtinterfacemutex': 'True',
      'sapluginmgmtipdomainname': 'True',
      'smartagentclientwaitforserver': 2000,
      'smartagentcmretrysend': 'True',
      'smartagentclientisunified': 'True',
      'smartagentcmclient': 'True',
      'smartagentclientname': 'UnifiedClient',
      'builtinencryption': 'True',
      'enableoninit': 'True',
      'routingreadybyevent': 'True',
      'systeminitbyevent': 'True',
      'smarttransportserveridcheck': 'True',
      'smarttransportproxysupport': 'True',
      'smartagentreportonupgrade': 'False',
      'smartagentusagestatisticsenable': 'False',
      'smartagentmaxrummemory': 50,
      'smartagentconcurrentthreadmax': 10,
      'smartagentpolicycontrollermodel': 'False',
      'smartagentpolicymodel': 'True',
      'smartagentfederallicense': 'True',
      'smartagentmultitenant': 'False',
      'attr365dayevalsyslog': 'True',
      'checkpointwriteonly': 'False',
      'smartagentdelaycertvalidation': 'False',
      'enablebydefault': 'False',
      'conversionautomatic': 'False',
      'conversionallowed': 'False',
      'storageencryptdisable': 'False',
      'storageloadunencrypteddisable': 'False',
      'tsplugindisable': 'False',
      'bypassudicheck': 'False',
      'loggingaddtstamp': 'False',
      'loggingaddtid': 'True',
      'highavailabilityoverrideevent': 'UnknownPlatformEvent',
      'platformindependentoverrideevent': 'UnknownPlatformEvent',
      'platformoverrideevent': 'SmartAgentSystemDataListChanged',
      'waitforharole': 'False',
      'standbyishot': 'True',
      'chkpttype': 2,
      'delaycomminit': 'False',
      'rolebyevent': 'True',
      'maxtracelength': 150,
      'tracealwayson': 'True',
      'debugflags': 0,
      'event_log_max_size': '5120 KB',
      'event_log_current_size': '21 KB',
      'trust_data': {
          'fxs2119q2u7:': {'p': 'C9407R',
          'trustvalue': 'Trust Data INSTALLED'}},
      'overall_trust': 'INSTALLED (2)',
      'clock_synced_with_ntp': 'True'},
 'platform_provided_mapping_table': {
    'pid': 'C9407R',
    'total_licenses_found': 163,
    'enforced_licenses': {
        'fxs2119q2u7': {
            'pid': 'C9407R'}}}}