## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):

    lte_module_dependencies = ['core', 'network', 'spectrum', 'stats', 'buildings', 'virtual-net-device','point-to-point','applications','internet','csma']
    if (bld.env['ENABLE_EMU']):
        lte_module_dependencies.append('fd-net-device')
    module = bld.create_ns3_module('lte', lte_module_dependencies)
    module.source = [
        'model/lte-common.cc',
        'model/lte-spectrum-phy.cc',
        'model/lte-spectrum-signal-parameters.cc',
        'model/lte-phy.cc',
        'model/lte-enb-phy.cc',
        'model/lte-ue-phy.cc',
        'model/lte-spectrum-value-helper.cc',
        'model/lte-amc.cc',
        'model/lte-enb-rrc.cc',
        'model/lte-ue-rrc.cc',
        'model/lte-rrc-sap.cc',
        'model/lte-rrc-protocol-ideal.cc',
        'model/lte-rrc-protocol-real.cc',
        'model/lte-rlc-sap.cc',
        'model/lte-rlc.cc',
        'model/lte-rlc-sequence-number.cc',
        'model/lte-rlc-header.cc',
        'model/lte-rlc-am-header.cc',
        'model/lte-rlc-tm.cc',
        'model/lte-rlc-um.cc',
        'model/lte-rlc-am.cc',
        'model/lte-rlc-tag.cc',
        'model/lte-rlc-sdu-status-tag.cc',
        'model/lte-pdcp-sap.cc',
        'model/lte-pdcp.cc',
        'model/lte-pdcp-header.cc',
        'model/lte-pdcp-tag.cc',
        'model/eps-bearer.cc',
        'model/lte-radio-bearer-info.cc',
        'model/lte-net-device.cc',
        'model/lte-enb-net-device.cc',
        'model/lte-ue-net-device.cc',
        'model/lte-control-messages.cc',
        'helper/lte-helper.cc',
        'helper/lte-stats-calculator.cc',
        'helper/epc-helper.cc',
        'helper/point-to-point-epc-helper.cc',
        'helper/radio-bearer-stats-calculator.cc',
        'helper/radio-bearer-stats-connector.cc',
        'helper/phy-stats-calculator.cc',
        'helper/mac-stats-calculator.cc',
        'helper/phy-tx-stats-calculator.cc',
        'helper/phy-rx-stats-calculator.cc',
        'helper/radio-environment-map-helper.cc',
        'helper/lte-hex-grid-enb-topology-helper.cc',
        'helper/lte-global-pathloss-database.cc',
        'helper/ra-preamble-phy-stats-calculator.cc',
        'helper/ra-preamble-stats-calculator.cc',
        'helper/ra-complete-stats-calculator.cc',
        'model/rem-spectrum-phy.cc',
        'model/ff-mac-common.cc',
        'model/ff-mac-csched-sap.cc',
        'model/ff-mac-sched-sap.cc',
        'model/lte-mac-sap.cc',
        'model/ff-mac-scheduler.cc',
        'model/lte-enb-cmac-sap.cc',
        'model/lte-ue-cmac-sap.cc',
        'model/rr-ff-mac-scheduler.cc',
        'model/lte-enb-mac.cc',
        'model/lte-ue-mac.cc',
        'model/lte-radio-bearer-tag.cc',
        'model/eps-bearer-tag.cc',
        'model/lte-phy-tag.cc',
        'model/lte-enb-phy-sap.cc',
        'model/lte-enb-cphy-sap.cc',
        'model/lte-ue-phy-sap.cc',
        'model/lte-ue-cphy-sap.cc',
        'model/lte-interference.cc',
        'model/lte-chunk-processor.cc',
        'model/pf-ff-mac-scheduler.cc',
        'model/fdmt-ff-mac-scheduler.cc',
        'model/tdmt-ff-mac-scheduler.cc',
        'model/tta-ff-mac-scheduler.cc',
        'model/fdbet-ff-mac-scheduler.cc',
        'model/tdbet-ff-mac-scheduler.cc',
        'model/fdtbfq-ff-mac-scheduler.cc',
        'model/tdtbfq-ff-mac-scheduler.cc',
        'model/pss-ff-mac-scheduler.cc',
        'model/cqa-ff-mac-scheduler.cc',
        'model/epc-gtpu-header.cc',
        'model/trace-fading-loss-model.cc',
        'model/epc-enb-application.cc',
        'model/epc-sgw-pgw-application.cc',
        'model/epc-x2-sap.cc',
        'model/epc-x2-header.cc',
        'model/epc-x2.cc',
        'model/epc-tft.cc',
        'model/epc-tft-classifier.cc',
        'model/lte-mi-error-model.cc',
        'model/lte-vendor-specific-parameters.cc',
        'model/epc-enb-s1-sap.cc',
        'model/epc-s1ap-sap.cc',
        'model/epc-s11-sap.cc',
        'model/lte-as-sap.cc',
        'model/epc-ue-nas.cc',
        'model/lte-harq-phy.cc',
        'model/epc-mme.cc',
        'model/lte-asn1-header.cc',
        'model/lte-rrc-header.cc',
        'model/lte-handover-management-sap.cc',
        'model/lte-handover-algorithm.cc',
        'model/a2-a4-rsrq-handover-algorithm.cc',
        'model/a3-rsrp-handover-algorithm.cc',
        'model/no-op-handover-algorithm.cc',
        'model/lte-anr-sap.cc',
        'model/lte-anr.cc',
        'model/lte-ffr-algorithm.cc',
        'model/lte-ffr-sap.cc',
        'model/lte-ffr-rrc-sap.cc',
        'model/lte-fr-no-op-algorithm.cc',
        'model/lte-fr-hard-algorithm.cc',
        'model/lte-fr-strict-algorithm.cc',
        'model/lte-fr-soft-algorithm.cc',
        'model/lte-ffr-soft-algorithm.cc',
        'model/lte-ffr-enhanced-algorithm.cc',
        'model/lte-ffr-distributed-algorithm.cc',
        'model/lte-ue-power-control.cc',
        'model/lte-interference-multiple-rx.cc',
        'model/lte-chunk-processor-multiple.cc',
        'model/lte-prach-info.cc',
        'model/epc-s1ap-header.cc',
        'model/epc-s1ap.cc'
        ]

    module_test = bld.create_ns3_module_test_library('lte')
    module_test.source = [
        'test/lte-test-downlink-sinr.cc',
        'test/lte-test-uplink-sinr.cc',
        'test/lte-test-link-adaptation.cc',
        'test/lte-test-interference.cc',
        'test/lte-test-ue-phy.cc',
        'test/lte-test-rr-ff-mac-scheduler.cc',
        'test/lte-test-pf-ff-mac-scheduler.cc',
        'test/lte-test-fdmt-ff-mac-scheduler.cc',
        'test/lte-test-tdmt-ff-mac-scheduler.cc',
        'test/lte-test-tta-ff-mac-scheduler.cc',
        'test/lte-test-fdbet-ff-mac-scheduler.cc',
        'test/lte-test-tdbet-ff-mac-scheduler.cc',
        'test/lte-test-fdtbfq-ff-mac-scheduler.cc',
        'test/lte-test-tdtbfq-ff-mac-scheduler.cc',
        'test/lte-test-pss-ff-mac-scheduler.cc',
        'test/lte-test-cqa-ff-mac-scheduler.cc',
        'test/lte-test-earfcn.cc',
        'test/lte-test-spectrum-value-helper.cc',
        'test/lte-test-pathloss-model.cc',
        'test/lte-test-entities.cc',
        'test/lte-simple-helper.cc',
        'test/lte-simple-net-device.cc',
        'test/test-lte-rlc-header.cc',
        'test/lte-test-rlc-um-transmitter.cc',
        'test/lte-test-rlc-am-transmitter.cc',
        'test/lte-test-rlc-um-e2e.cc',
        'test/lte-test-rlc-am-e2e.cc',
        'test/epc-test-gtpu.cc',
        'test/test-epc-tft-classifier.cc',
        'test/epc-test-s1u-downlink.cc',
        'test/epc-test-s1u-uplink.cc',
        'test/test-lte-epc-e2e-data.cc',
        'test/test-lte-antenna.cc',
        'test/lte-test-phy-error-model.cc',
        'test/lte-test-mimo.cc',
        'test/lte-test-harq.cc',
        'test/test-lte-rrc.cc',
        'test/test-lte-x2-handover.cc',
        'test/test-lte-x2-handover-measures.cc',
        'test/test-asn1-encoding.cc',
        'test/lte-test-ue-measurements.cc',
        'test/lte-test-cell-selection.cc',
        'test/test-lte-handover-delay.cc',
        'test/test-lte-handover-target.cc',
        'test/lte-test-deactivate-bearer.cc',
        'test/lte-ffr-simple.cc',
        'test/lte-test-downlink-power-control.cc',
        'test/lte-test-uplink-power-control.cc',
        'test/lte-test-frequency-reuse.cc',
        'test/lte-test-interference-fr.cc',
        'test/lte-test-cqi-generation.cc',
        'test/lte-simple-spectrum-phy.cc',
        ]

    headers = bld(features='ns3header')
    headers.module = 'lte'
    headers.source = [
        'model/lte-common.h',
        'model/lte-spectrum-phy.h',
        'model/lte-spectrum-signal-parameters.h',
        'model/lte-phy.h',
        'model/lte-enb-phy.h',
        'model/lte-ue-phy.h',
        'model/lte-spectrum-value-helper.h',
        'model/lte-amc.h',
        'model/lte-enb-rrc.h',
        'model/lte-ue-rrc.h',
        'model/lte-rrc-sap.h',
        'model/lte-rrc-protocol-ideal.h',
        'model/lte-rrc-protocol-real.h',
        'model/lte-rlc-sap.h',
        'model/lte-rlc.h',
        'model/lte-rlc-header.h',
        'model/lte-rlc-sequence-number.h',
        'model/lte-rlc-am-header.h',
        'model/lte-rlc-tm.h',
        'model/lte-rlc-um.h',
        'model/lte-rlc-am.h',
        'model/lte-rlc-tag.h',
        'model/lte-rlc-sdu-status-tag.h',
        'model/lte-pdcp-sap.h',
        'model/lte-pdcp.h',
        'model/lte-pdcp-header.h',
        'model/lte-pdcp-tag.h',
        'model/eps-bearer.h',
        'model/lte-radio-bearer-info.h',
        'model/lte-net-device.h',
        'model/lte-enb-net-device.h',
        'model/lte-ue-net-device.h',
        'model/lte-control-messages.h',
        'helper/lte-helper.h',
        'helper/lte-stats-calculator.h',
        'helper/epc-helper.h',
        'helper/point-to-point-epc-helper.h',
        'helper/phy-stats-calculator.h',
        'helper/mac-stats-calculator.h',
        'helper/phy-tx-stats-calculator.h',
        'helper/phy-rx-stats-calculator.h',
        'helper/radio-bearer-stats-calculator.h',
        'helper/radio-bearer-stats-connector.h',
        'helper/radio-environment-map-helper.h',
        'helper/lte-hex-grid-enb-topology-helper.h',
        'helper/lte-global-pathloss-database.h',
        'helper/ra-preamble-phy-stats-calculator.h',
        'helper/ra-preamble-stats-calculator.h',
        'helper/ra-complete-stats-calculator.h',
        'model/rem-spectrum-phy.h',
        'model/ff-mac-common.h',
        'model/ff-mac-csched-sap.h',
        'model/ff-mac-sched-sap.h',
        'model/lte-enb-cmac-sap.h',
        'model/lte-ue-cmac-sap.h',
        'model/lte-mac-sap.h',
        'model/ff-mac-scheduler.h',
        'model/rr-ff-mac-scheduler.h',
        'model/lte-enb-mac.h',
        'model/lte-ue-mac.h',
        'model/lte-radio-bearer-tag.h',
        'model/eps-bearer-tag.h',
        'model/lte-phy-tag.h',
        'model/lte-enb-phy-sap.h',
        'model/lte-enb-cphy-sap.h',
        'model/lte-ue-phy-sap.h',
        'model/lte-ue-cphy-sap.h',
        'model/lte-interference.h',
        'model/lte-chunk-processor.h',
        'model/pf-ff-mac-scheduler.h',
        'model/fdmt-ff-mac-scheduler.h',
        'model/tdmt-ff-mac-scheduler.h',
        'model/tta-ff-mac-scheduler.h',
        'model/fdbet-ff-mac-scheduler.h',
        'model/tdbet-ff-mac-scheduler.h',
        'model/fdtbfq-ff-mac-scheduler.h',
        'model/tdtbfq-ff-mac-scheduler.h',
        'model/pss-ff-mac-scheduler.h',
        'model/cqa-ff-mac-scheduler.h',
        'model/trace-fading-loss-model.h',
        'model/epc-gtpu-header.h',
        'model/epc-enb-application.h',
        'model/epc-sgw-pgw-application.h',
        'model/lte-vendor-specific-parameters.h',
        'model/epc-x2-sap.h',
        'model/epc-x2-header.h',
        'model/epc-x2.h',
        'model/epc-tft.h',
        'model/epc-tft-classifier.h',
        'model/lte-mi-error-model.h',
        'model/epc-enb-s1-sap.h',
        'model/epc-s1ap-sap.h',
        'model/epc-s11-sap.h',
        'model/lte-as-sap.h',
        'model/epc-ue-nas.h',
        'model/lte-harq-phy.h',
        'model/epc-mme.h',
        'model/lte-asn1-header.h',
        'model/lte-rrc-header.h',
        'model/lte-handover-management-sap.h',
        'model/lte-handover-algorithm.h',
        'model/a2-a4-rsrq-handover-algorithm.h',
        'model/a3-rsrp-handover-algorithm.h',
        'model/no-op-handover-algorithm.h',
        'model/lte-anr-sap.h',
        'model/lte-anr.h',
        'model/lte-ffr-algorithm.h',
        'model/lte-ffr-sap.h',
        'model/lte-ffr-rrc-sap.h',
        'model/lte-fr-no-op-algorithm.h',
        'model/lte-fr-hard-algorithm.h',
        'model/lte-fr-strict-algorithm.h',
        'model/lte-fr-soft-algorithm.h',
        'model/lte-ffr-soft-algorithm.h',
        'model/lte-ffr-enhanced-algorithm.h',
        'model/lte-ffr-distributed-algorithm.h',     
        'model/lte-ue-power-control.h',   
        'model/lte-interference-multiple-rx.h',     
        'model/lte-chunk-processor-multiple.h', 
        'model/lte-prach-info.h',
        'model/epc-s1ap-header.h',
        'model/epc-s1ap.h'
        ]

    if (bld.env['ENABLE_EMU']):
        module.source.append ('helper/emu-epc-helper.cc')
        headers.source.append ('helper/emu-epc-helper.h')

    if (bld.env['ENABLE_EXAMPLES']):
      bld.recurse('examples')

    bld.ns3_python_bindings()
