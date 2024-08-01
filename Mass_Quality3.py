#!/usr/bin/python
#@author - Sasidhar
import sys
import csv
import os
import time

from ConfigParser import SafeConfigParser
Example = ("Usage:python Mass_2.py <Mass query output folder> <headers file>"
"\n"
"E.G:"
"\n"
"\n"
"python Mass_Quality.py mass_ouput headers.ini")

if len(sys.argv) < 3:
        print("Number of aruguments should be 3")
        print
        print Example
        sys.exit()


mass_output = sys.argv[1]

parser_1 = SafeConfigParser()
parser_1.read(sys.argv[2])

header = parser_1.get('Headers', 'header').split(',')

imsi_head = header[0].strip()
msisdn_head = header[1].strip()
imei_head = header[2].strip()
carrier_head = header[12].strip()
event_head = header[9].strip()
loc_head = header[4].strip()
rat_head = header[11].strip()
cgi_head = header[10].strip()
bparty_head = header[16].strip()

testname = raw_input('Please enter the directory name where output files needs to be copied:')
if not os.path.isfile(testname) and not os.path.isdir(testname):
    os.mkdir(testname)
testPath=os.getcwd()+'/'+testname

kpidic= {}

for rat_value in ['GSM','UMTS','LTE']:
    for loc_value in ['WLS','ECID','CID','AGPS','HYBRID','OTHERS','SWITCH']:
        for event_value in ['LOCATIONUPDATE','MO SMS','MT SMS','IMSIATTACH','IMSIDETACH','VOICE CALL START','VOICE CALL END','MT LR','MOCS','MTCE','MTCS','MOCE','HO','CS','CE','MOVOICECALLSTART','MTVOICECALLSTART','MOVOICECALLEND','MTVOICECALLEND','MOVOICECALLATTEMPT','MTVOICECALLATTEMPT']:
            key = rat_value+'-'+loc_value+'-'+event_value
            kpidic[key] = 0
imsi_dict = {}
msisdn_dict = {}
imei_dict = {}
uniq_dict = {}
uniq_cgi = {}

start_time = time.time()

imsi_omd_len1 = 0;imsi_omd_len2 = 0;imsi_omd_len3 = 0;imsi_omd_len4 = 0;imsi_omd_len5 = 0;imsi_omd_len6 = 0;imsi_omd_len7 = 0;imsi_omd_len8 = 0;imsi_omd_len9 = 0;imsi_omd_len10 = 0;imsi_omd_len11 = 0;imsi_omd_len12 = 0;imsi_omd_len13 = 0;imsi_omd_len14 = 0;imsi_omd_len15 = 0;imsi_omd_len16 = 0;imsi_ord_len1 = 0;imsi_ord_len2 = 0;imsi_ord_len3 = 0;imsi_ord_len4 = 0;imsi_ord_len5 = 0;imsi_ord_len6 = 0;imsi_ord_len7 = 0;imsi_ord_len8 = 0;imsi_ord_len9 = 0;imsi_ord_len10 = 0;imsi_ord_len11 = 0;imsi_ord_len12 = 0;imsi_ord_len13 = 0;imsi_ord_len14 = 0;imsi_ord_len15 = 0;imsi_ord_len16 = 0;imsi_omf_len1 = 0;imsi_omf_len2 = 0;imsi_omf_len3 = 0;imsi_omf_len4 = 0;imsi_omf_len5 = 0;imsi_omf_len6 = 0;imsi_omf_len7 = 0;imsi_omf_len8 = 0;imsi_omf_len9 = 0;imsi_omf_len10 = 0;imsi_omf_len11 = 0;imsi_omf_len12 = 0;imsi_omf_len13 = 0;imsi_omf_len14 = 0;imsi_omf_len15 = 0;imsi_omf_len16 = 0;imsi_orf_len1 = 0;imsi_orf_len2 = 0;imsi_orf_len3 = 0;imsi_orf_len4 = 0;imsi_orf_len5 = 0;imsi_orf_len6 = 0;imsi_orf_len7 = 0;imsi_orf_len8 = 0;imsi_orf_len9 = 0;imsi_orf_len10 = 0;imsi_orf_len11 = 0;imsi_orf_len12 = 0;imsi_orf_len13 = 0;imsi_orf_len14 = 0;imsi_orf_len15 = 0;imsi_orf_len16 = 0;msisdn_omd_len1 = 0;msisdn_omd_len2 = 0;msisdn_omd_len3 = 0;msisdn_omd_len4 = 0;msisdn_omd_len5 = 0;msisdn_omd_len6 = 0;msisdn_omd_len7 = 0;msisdn_omd_len8 = 0;msisdn_omd_len9 = 0;msisdn_omd_len10 = 0;msisdn_omd_len11 = 0;msisdn_omd_len12 = 0;msisdn_omd_len13 = 0;msisdn_omd_len14 = 0;msisdn_omd_len15 = 0;msisdn_omd_len16 = 0;msisdn_omf_len1 = 0;msisdn_omf_len2 = 0;msisdn_omf_len3 = 0;msisdn_omf_len4 = 0;msisdn_omf_len5 = 0;msisdn_omf_len6 = 0;msisdn_omf_len7 = 0;msisdn_omf_len8 = 0;msisdn_omf_len9 = 0;msisdn_omf_len10 = 0;msisdn_omf_len11 = 0;msisdn_omf_len12 = 0;msisdn_omf_len13 = 0;msisdn_omf_len14 = 0;msisdn_omf_len15 = 0;msisdn_omf_len16 = 0;msisdn_ord_len1 = 0;msisdn_ord_len2 = 0;msisdn_ord_len3 = 0;msisdn_ord_len4 = 0;msisdn_ord_len5 = 0;msisdn_ord_len6 = 0;msisdn_ord_len7 = 0;msisdn_ord_len8 = 0;msisdn_ord_len9 = 0;msisdn_ord_len10 = 0;msisdn_ord_len11 = 0;msisdn_ord_len12 = 0;msisdn_ord_len13 = 0;msisdn_ord_len14 = 0;msisdn_ord_len15 = 0;msisdn_ord_len16 = 0;msisdn_orf_len1 = 0;msisdn_orf_len2 = 0;msisdn_orf_len3 = 0;msisdn_orf_len4 = 0;msisdn_orf_len5 = 0;msisdn_orf_len6 = 0;msisdn_orf_len7 = 0;msisdn_orf_len8 = 0;msisdn_orf_len9 = 0;msisdn_orf_len10 = 0;msisdn_orf_len11 = 0;msisdn_orf_len12 = 0;msisdn_orf_len13 = 0;msisdn_orf_len14 = 0;msisdn_orf_len15 = 0;msisdn_orf_len16 = 0;imei_omf_len1 = 0;imei_omf_len2 = 0;imei_omf_len3 = 0;imei_omf_len4 = 0;imei_omf_len5 = 0;imei_omf_len6 = 0;imei_omf_len7 = 0;imei_omf_len8 = 0;imei_omf_len9 = 0;imei_omf_len10 = 0;imei_omf_len11 = 0;imei_omf_len17 = 0;imei_omf_len12 = 0;imei_omf_len13 = 0;imei_omf_len14 = 0;imei_omf_len15 = 0;imei_omf_len16 = 0;gsm_cgi_len1 = 0;gsm_cgi_len2 = 0;gsm_cgi_len3 = 0;gsm_cgi_len4 = 0;gsm_cgi_len5 = 0;gsm_cgi_len6 = 0;gsm_cgi_len7 = 0;gsm_cgi_len8 = 0;gsm_cgi_len9 = 0;gsm_cgi_len10 = 0;gsm_cgi_len11 = 0;gsm_cgi_len12 = 0;gsm_cgi_len13 = 0;gsm_cgi_len17 = 0;gsm_cgi_len14 = 0;gsm_cgi_len15 = 0;gsm_cgi_len16 = 0;umts_cgi_len14 = 0;umts_cgi_len15 = 0;umts_cgi_len16 = 0;lte_cgi_len14 = 0;lte_cgi_len15 = 0;lte_cgi_len16 = 0;imei_omd_len1 = 0;imei_omd_len2 = 0;imei_omd_len3 = 0;imei_omd_len4 = 0;imei_omd_len5 = 0;imei_omd_len6 = 0;imei_omd_len7 = 0;imei_omd_len8 = 0;imei_omd_len9 = 0;imei_omd_len10 = 0;imei_omd_len11 = 0;imei_omd_len17 = 0;imei_omd_len12 = 0;imei_omd_len13 = 0;imei_omd_len14 = 0;imei_omd_len15 = 0;imei_omd_len16 = 0;imei_ord_len1 = 0;imei_ord_len2 = 0;imei_ord_len3 = 0;imei_ord_len4 = 0;imei_ord_len5 = 0;imei_ord_len6 = 0;imei_ord_len7 = 0;imei_ord_len8 = 0;imei_ord_len9 = 0;imei_ord_len10 = 0;imei_ord_len11 = 0;imei_ord_len17 = 0;imei_ord_len12 = 0;imei_ord_len13 = 0;imei_ord_len14 = 0;imei_ord_len15 = 0;imei_ord_len16 = 0;imei_orf_len1 = 0;imei_orf_len2 = 0;imei_orf_len3 = 0;imei_orf_len4 = 0;imei_orf_len5 = 0;imei_orf_len6 = 0;imei_orf_len7 = 0;imei_orf_len8 = 0;imei_orf_len9 = 0;imei_orf_len10 = 0;imei_orf_len11 = 0;imei_orf_len12 = 0;imei_orf_len13 = 0;imei_orf_len14 = 0;imei_orf_len15 = 0;imei_orf_len16 = 0;imei_orf_len17 = 0

def mass_analysis(mass_query):
    unique_set_msisdn = set()
    unique_set_imei = set()
    unique_set_msisdn_imei = set()
    unique_set_msisdn_OM = set()
    unique_set_msisdn_OM_FR = set()
    unique_set_msisdn_OR = set()
    unique_set_msisdn_OR_FR = set()
    unique_set_imei_OM = set()
    unique_set_imei_OM_FR = set()
    unique_set_imei_OR = set()
    unique_set_imei_OR_FR = set()
    unique_set_msisdn_imei_OM = set()
    unique_set_msisdn_imei_OM_FR = set()
    unique_set_msisdn_imei_OR = set()
    unique_set_msisdn_imei_OR_FR = set()
    unique_set_domestic_roamer_OM = set()
    unique_set_domestic_roamer_OR = set()
    unique_set_gsm_cgi_1 = set()
    unique_set_gsm_cgi_2 = set()
    unique_set_gsm_cgi_3 = set()
    unique_set_gsm_cgi_4 = set()
    unique_set_gsm_cgi_5 = set()
    unique_set_gsm_cgi_6 = set()
    unique_set_gsm_cgi_7 = set()
    unique_set_gsm_cgi_8 = set()
    unique_set_gsm_cgi_9 = set()
    unique_set_gsm_cgi_10 = set()
    unique_set_gsm_cgi_11 = set()
    unique_set_gsm_cgi_12 = set()
    unique_set_gsm_cgi_13 = set()
    unique_set_gsm_cgi_17 = set()
    unique_set_gsm_cgi_14 = set()
    unique_set_gsm_cgi_15 = set()
    unique_set_gsm_cgi_16 = set()
    unique_set_umts_cgi_1 = set()
    unique_set_umts_cgi_2 = set()
    unique_set_umts_cgi_3 = set()
    unique_set_umts_cgi_4 = set()
    unique_set_umts_cgi_5 = set()
    unique_set_umts_cgi_6 = set()
    unique_set_umts_cgi_7 = set()
    unique_set_umts_cgi_8 = set()
    unique_set_umts_cgi_9 = set()
    unique_set_umts_cgi_10 = set()
    unique_set_umts_cgi_11 = set()
    unique_set_umts_cgi_12 = set()
    unique_set_umts_cgi_13 = set()
    unique_set_umts_cgi_17 = set()
    unique_set_umts_cgi_14 = set()
    unique_set_umts_cgi_15 = set()
    unique_set_umts_cgi_16 = set()
    unique_set_lte_cgi_1 = set()
    unique_set_lte_cgi_2 = set()
    unique_set_lte_cgi_3 = set()
    unique_set_lte_cgi_4 = set()
    unique_set_lte_cgi_5 = set()
    unique_set_lte_cgi_6 = set()
    unique_set_lte_cgi_7 = set()
    unique_set_lte_cgi_8 = set()
    unique_set_lte_cgi_9 = set()
    unique_set_lte_cgi_10 = set()
    unique_set_lte_cgi_11 = set()
    unique_set_lte_cgi_12 = set()
    unique_set_lte_cgi_13 = set()
    unique_set_lte_cgi_17 = set()
    unique_set_lte_cgi_14 = set()
    unique_set_lte_cgi_15 = set()
    unique_set_lte_cgi_16 = set()
    unique_set_imsi_om = set()
    unique_set_imsi_om_other_empty = set()
    unique_set_imsi_or = set()
    unique_set_imsi_or_other_empty = set()
    unique_set_foreign_imsi = set()
    unique_set_foreign_imsi_other_empty = set()


    global total_records;global imsi_msisdn_count;global imsi_imei_count;global imsi_imei_msisdn_count;global imsi_imei_or_count;global imsi_msisdn_or_count;global imsi_imei_msisdn_or_count;global imsi_imei_om_count;global imsi_msisdn_om_count;global imsi_imei_msisdn_om_count;global foreign_imsi_with_msisdn_om;global foreign_imsi_with_msisdn_or;global domestic_roamer_om;global domestic_roamer_or;global imei_domestic_roamer_om;global imei_domestic_roamer_or;global msisdn_imei_domestic_roamer_om;global msisdn_imei_domestic_roamer_or;global foreign_imsi_with_imei_om;global foreign_imsi_with_imei_or;global foreign_imsi_imei_msisdn_om;global foreign_imsi_imei_msisdn_or;global mosms_bparty;global mtsms_bparty;global vcs_bparty;global vce_bparty;global total_vcs;global total_vce;global total_mtsms;global total_mosms;global gsm_cgi_len1;global gsm_cgi_len2;global gsm_cgi_len3;global gsm_cgi_len4;global gsm_cgi_len5;global gsm_cgi_len6;global gsm_cgi_len7;global gsm_cgi_len8;global gsm_cgi_len9;global gsm_cgi_len10;global gsm_cgi_len11;global gsm_cgi_len12;global gsm_cgi_len13;global gsm_cgi_len17;global gsm_cgi_len14;global gsm_cgi_len15;global gsm_cgi_len16;global umts_cgi_len1;global umts_cgi_len2;global umts_cgi_len3;global umts_cgi_len4;global umts_cgi_len5;global umts_cgi_len6;global umts_cgi_len7;global umts_cgi_len8;global umts_cgi_len9;global umts_cgi_len10;global umts_cgi_len11;global umts_cgi_len12;global umts_cgi_len13;global umts_cgi_len17;global umts_cgi_len14;global umts_cgi_len15;global umts_cgi_len16;global lte_cgi_len1;global lte_cgi_len2;global lte_cgi_len3;global lte_cgi_len4;global lte_cgi_len5;global lte_cgi_len6;global lte_cgi_len7;global lte_cgi_len8;global lte_cgi_len9;global lte_cgi_len10;global lte_cgi_len11;global lte_cgi_len12;global lte_cgi_len13;global lte_cgi_len17;global lte_cgi_len14;global lte_cgi_len15;global lte_cgi_len16;global mosms_bparty_omd;global mtsms_bparty_omd;global vcs_bparty_omd;global vce_bparty_omd;global mosms_bparty_ominroamers;global mtsms_bparty_ominroamers;global vcs_bparty_ominroamers;global vce_bparty_ominroamers;global mosms_bparty_omf;global mtsms_bparty_omf;global vcs_bparty_omf;global vce_bparty_omf;global mosms_bparty_ord;global mtsms_bparty_ord;global vcs_bparty_ord;global vce_bparty_ord;global mosms_bparty_orinroamers;global mtsms_bparty_orinroamers;global vcs_bparty_orinroamers;global vce_bparty_orinroamers;global mosms_bparty_orf;global mtsms_bparty_orf;global vcs_bparty_orf;global vce_bparty_orf
    total_records = 0;imsi_msisdn_count = 0;imsi_imei_count = 0;imsi_imei_msisdn_count = 0;imsi_imei_or_count = 0;imsi_msisdn_or_count = 0;imsi_imei_msisdn_or_count = 0;imsi_imei_om_count = 0;imsi_msisdn_om_count = 0;imsi_imei_msisdn_om_count = 0;foreign_imsi_with_msisdn_om = 0;foreign_imsi_with_msisdn_or = 0;domestic_roamer_om = 0;domestic_roamer_or = 0;imei_domestic_roamer_om = 0;imei_domestic_roamer_or = 0;msisdn_imei_domestic_roamer_om = 0;msisdn_imei_domestic_roamer_or = 0;foreign_imsi_with_imei_om = 0;foreign_imsi_with_imei_or = 0;foreign_imsi_imei_msisdn_om = 0;foreign_imsi_imei_msisdn_or = 0;mosms_bparty =0;mtsms_bparty = 0;vcs_bparty = 0;vce_bparty = 0;total_vcs = 0;total_vce = 0;total_mtsms = 0;total_mosms = 0;gsm_cgi_len1 = 0;gsm_cgi_len2 = 0;gsm_cgi_len3 = 0;gsm_cgi_len4 = 0;gsm_cgi_len5 = 0;gsm_cgi_len6 = 0;gsm_cgi_len7 = 0;gsm_cgi_len8 = 0;gsm_cgi_len9 = 0;gsm_cgi_len10 = 0;gsm_cgi_len11 = 0;gsm_cgi_len12 = 0;gsm_cgi_len13 = 0;gsm_cgi_len17 = 0;gsm_cgi_len14 = 0;gsm_cgi_len15 = 0;gsm_cgi_len16 = 0;umts_cgi_len1 = 0;umts_cgi_len2 = 0;umts_cgi_len3 = 0;umts_cgi_len4 = 0;umts_cgi_len5 = 0;umts_cgi_len6 = 0;umts_cgi_len7 = 0;umts_cgi_len8 = 0;umts_cgi_len9 = 0;umts_cgi_len10 = 0;umts_cgi_len11 = 0;umts_cgi_len12 = 0;umts_cgi_len13 = 0;umts_cgi_len17 = 0;umts_cgi_len14 = 0;umts_cgi_len15 = 0;umts_cgi_len16 = 0;lte_cgi_len1 = 0;lte_cgi_len2 = 0;lte_cgi_len3 = 0;lte_cgi_len4 = 0;lte_cgi_len5 = 0;lte_cgi_len6 = 0;lte_cgi_len7 = 0;lte_cgi_len8 = 0;lte_cgi_len9 = 0;lte_cgi_len10 = 0;lte_cgi_len11 = 0;lte_cgi_len12 = 0;lte_cgi_len13 = 0;lte_cgi_len17 = 0;lte_cgi_len14 = 0;lte_cgi_len15 = 0;lte_cgi_len16 = 0;mosms_bparty_omd = 0;mtsms_bparty_omd = 0;vcs_bparty_omd = 0;vce_bparty_omd = 0;mosms_bparty_ominroamers = 0;mtsms_bparty_ominroamers = 0;vcs_bparty_ominroamers = 0;vce_bparty_ominroamers = 0;mosms_bparty_omf = 0;mtsms_bparty_omf = 0;vcs_bparty_omf = 0;vce_bparty_omf = 0;mosms_bparty_ord = 0;mtsms_bparty_ord = 0;vcs_bparty_ord = 0;vce_bparty_ord = 0;mosms_bparty_orinroamers = 0;mtsms_bparty_orinroamers = 0;vcs_bparty_orinroamers = 0;vce_bparty_orinroamers = 0;mosms_bparty_orf = 0;mtsms_bparty_orf = 0;vcs_bparty_orf = 0;vce_bparty_orf = 0
    for filename in os.listdir(mass_query):
        if filename.endswith(".csv"):
            with open(mass_query+'/'+filename) as f:
                csvReader = csv.reader(f, delimiter = ',')
                for line in csvReader:
                    ln = csvReader.line_num

                    if ln == 1:

                        imsi_i = line.index(imsi_head)
                        msisdn_i = line.index(msisdn_head)
                        imei_i = line.index(imei_head)
                        carrier_i = line.index(carrier_head)
                        event_i = line.index(event_head)
                        loc_i = line.index(loc_head)
                        rat_i = line.index(rat_head)
                        cgi_i = line.index(cgi_head)
                        bparty_i = line.index(bparty_head)
                        continue
                    imsi = line[imsi_i]
                    msisdn = line[msisdn_i]
                    imei = line[imei_i]
                    carrier = line[carrier_i]
                    event1 = line[event_i]
                    loc = line[loc_i]
                    rat = line[rat_i]
                    cgi = line[cgi_i]

                    bparty = line[bparty_i]


                    if event1 == '':
                            continue
                    elif event1 == 'MO SMS' or event1 == '2':
                            event = 'MO SMS'
                    elif event1 == 'MT SMS' or event1 == '3':
                            event = 'MT SMS'
                    elif event1 == 'VOICE CALL START' or event1 == '7':
                            event = 'VOICE CALL START'
                    elif event1 == 'VOICE CALL END' or event1 == '8':
                            event = 'VOICE CALL END'
                    elif event1 == 'LOCATIONUPDATE' or event1 == '1':
                            event = 'LOCATIONUPDATE'
                    elif event1 == 'IMSIATTACH' or event1 == '5':
                            event = 'IMSIATTACH'
                    elif event1 == 'IMSIDETACH' or event1 == '6':
                            event = 'IMSIDETACH'
                    elif event1 == 'MT LR' or event1 == '9':
                            event = 'MT LR'
                    elif event1 == 'MOVOICECALLSTART' or event1 == '12':
                            event == 'MOVOICECALLSTART'
                    elif event1 == 'MTVOICECALLSTART' or event1 == '13':
                            event == 'MTVOICECALLSTART'
                    elif event1 == 'MOVOICECALLEND' or event1 == '14':
                            event == 'MOVOICECALLEND'
                    elif event1 == 'MTVOICECALLEND' or event1 == '15':
                            event = 'MTVOICECALLEND'
                    elif event1 == 'MOCS' or event1 == '16':
                            event = 'MOCS'
                    elif event1 == 'MOCE' or event1 == '17':
                            event = 'MOCE'
                    elif event1 == 'MTCS' or event1 == '18':
                            event = 'MTCS'
                    elif event1 == 'MTCE' or event1 == '19':
                            event = 'MTCE'
                    elif event1 == 'HO' or event1 == '20':
                            event = 'HO'
                    elif event1 == 'CS' or event1 == '21':
                            event = 'CS'
                    elif event1 == 'CE' or event1 == '22':
                            event = 'CE'
                    elif event1 == 'MOVOICECALLATTEMPT' or event1 == '10':
                            event = 'MOVOICECALLATTEMPT'
                    elif event1 == 'MTVOICECALLATTEMPT' or event1 == '11':
                            event = 'MTVOICECALLATTEMPT'

                    if rat == 'GSM' or rat == '1':
                            rat = 'GSM'
                            if cgi == 'NULL' or cgi == '':
                                pass
                            else:
                                uniq_dict[cgi+'_'+rat] = rat

                                if len(cgi) == 1:
                                    gsm_cgi_len1 += 1
                                    unique_set_gsm_cgi_1.add(line[10])
                                if len(cgi) == 2:
                                    gsm_cgi_len2 += 1
                                    unique_set_gsm_cgi_2.add(line[10])
                                if len(cgi) == 3:
                                    gsm_cgi_len3 += 1
                                    unique_set_gsm_cgi_3.add(line[10])
                                if len(cgi) == 4:
                                    gsm_cgi_len4 += 1
                                    unique_set_gsm_cgi_4.add(line[10])
                                if len(cgi) == 5:
                                    gsm_cgi_len5 += 1
                                    unique_set_gsm_cgi_5.add(line[10])
                                if len(cgi) == 6:
                                    gsm_cgi_len6 += 1
                                    unique_set_gsm_cgi_6.add(line[10])
                                if len(cgi) == 7:
                                    gsm_cgi_len7 += 1
                                    unique_set_gsm_cgi_7.add(line[10])
                                if len(cgi) == 8:
                                    gsm_cgi_len8 += 1
                                    unique_set_gsm_cgi_8.add(line[10])
                                if len(cgi) == 9:
                                    gsm_cgi_len9 += 1
                                    unique_set_gsm_cgi_9.add(line[10])
                                if len(cgi) == 10:
                                    gsm_cgi_len10 += 1
                                    unique_set_gsm_cgi_10.add(line[10])
                                if len(cgi) == 11:
                                    gsm_cgi_len11 += 1
                                    unique_set_gsm_cgi_11.add(line[10])
                                if len(cgi) == 12:
                                    gsm_cgi_len12 += 1
                                    unique_set_gsm_cgi_12.add(line[10])
                                if len(cgi) == 13:
                                    gsm_cgi_len13 += 1
                                    unique_set_gsm_cgi_13.add(line[10])

                                if len(cgi) == 14:
                                    gsm_cgi_len14 += 1
                                    unique_set_gsm_cgi_14.add(line[10])
                                if len(cgi) == 15:
                                    gsm_cgi_len15 += 1
                                    unique_set_gsm_cgi_15.add(line[10])
                                if len(cgi) == 16:
                                    gsm_cgi_len16 += 1
                                    unique_set_gsm_cgi_16.add(line[10])
                                if len(cgi) >= 17:
                                    gsm_cgi_len17 += 1
                                    unique_set_gsm_cgi_17.add(line[10])

                    elif rat == 'UMTS' or rat == '2':
                            rat = 'UMTS'
                            if cgi == 'NULL' or cgi == '':
                                pass
                            else:
                                uniq_dict[cgi+'_'+rat] = rat

                                if len(cgi) == 1:
                                    umts_cgi_len1 += 1
                                    unique_set_umts_cgi_1.add(line[10])
                                if len(cgi) == 2:
                                    umts_cgi_len2 += 1
                                    unique_set_umts_cgi_2.add(line[10])
                                if len(cgi) == 3:
                                    umts_cgi_len3 += 1
                                    unique_set_umts_cgi_3.add(line[10])
                                if len(cgi) == 4:
                                    umts_cgi_len4 += 1
                                    unique_set_umts_cgi_4.add(line[10])
                                if len(cgi) == 5:
                                    umts_cgi_len5 += 1
                                    unique_set_umts_cgi_5.add(line[10])
                                if len(cgi) == 6:
                                    umts_cgi_len6 += 1
                                    unique_set_umts_cgi_6.add(line[10])
                                if len(cgi) == 7:
                                    umts_cgi_len7 += 1
                                    unique_set_umts_cgi_7.add(line[10])
                                if len(cgi) == 8:
                                    umts_cgi_len8 += 1
                                    unique_set_umts_cgi_8.add(line[10])
                                if len(cgi) == 9:
                                    umts_cgi_len9 += 1
                                    unique_set_umts_cgi_9.add(line[10])
                                if len(cgi) == 10:
                                    umts_cgi_len10 += 1
                                    unique_set_umts_cgi_10.add(line[10])
                                if len(cgi) == 11:
                                    umts_cgi_len11 += 1
                                    unique_set_umts_cgi_11.add(line[10])
                                if len(cgi) == 12:
                                    umts_cgi_len12 += 1
                                    unique_set_umts_cgi_12.add(line[10])
                                if len(cgi) == 13:
                                    umts_cgi_len13 += 1
                                    unique_set_umts_cgi_13.add(line[10])

                                if len(cgi) == 14:
                                    umts_cgi_len14 += 1
                                    unique_set_umts_cgi_14.add(line[10])
                                if len(cgi) == 15:
                                    umts_cgi_len15 += 1
                                    unique_set_umts_cgi_15.add(line[10])
                                if len(cgi) == 16:
                                    umts_cgi_len16 += 1
                                    unique_set_umts_cgi_16.add(line[10])
                                if len(cgi) >= 17:
                                    umts_cgi_len17 += 1
                                    unique_set_umts_cgi_17.add(line[10])

                    elif rat == 'LTE' or rat == '3':
                            rat = 'LTE'
                            if cgi == 'NULL' or cgi == '':
                                pass
                            else:
                                uniq_dict[cgi+'_'+rat] = rat
                                if len(cgi) == 1:
                                    lte_cgi_len1 += 1
                                    unique_set_lte_cgi_1.add(line[10])
                                if len(cgi) == 2:
                                    lte_cgi_len2 += 1
                                    unique_set_lte_cgi_2.add(line[10])
                                if len(cgi) == 3:
                                    lte_cgi_len3 += 1
                                    unique_set_lte_cgi_3.add(line[10])
                                if len(cgi) == 4:
                                    lte_cgi_len4 += 1
                                    unique_set_lte_cgi_4.add(line[10])
                                if len(cgi) == 5:
                                    lte_cgi_len5 += 1
                                    unique_set_lte_cgi_5.add(line[10])
                                if len(cgi) == 6:
                                    lte_cgi_len6 += 1
                                    unique_set_lte_cgi_6.add(line[10])
                                if len(cgi) == 7:
                                    lte_cgi_len7 += 1
                                    unique_set_lte_cgi_7.add(line[10])
                                if len(cgi) == 8:
                                    lte_cgi_len8 += 1
                                    unique_set_lte_cgi_8.add(line[10])
                                if len(cgi) == 9:
                                    lte_cgi_len9 += 1
                                    unique_set_lte_cgi_9.add(line[10])
                                if len(cgi) == 10:
                                    lte_cgi_len10 += 1
                                    unique_set_lte_cgi_10.add(line[10])
                                if len(cgi) == 11:
                                    lte_cgi_len11 += 1
                                    unique_set_lte_cgi_11.add(line[10])
                                if len(cgi) == 12:
                                    lte_cgi_len12 += 1
                                    unique_set_lte_cgi_12.add(line[10])
                                if len(cgi) == 13:
                                    lte_cgi_len13 += 1
                                    unique_set_lte_cgi_13.add(line[10])

                                if len(cgi) == 14:
                                    lte_cgi_len14 += 1
                                    unique_set_lte_cgi_14.add(line[10])
                                if len(cgi) == 15:
                                    lte_cgi_len15 += 1
                                    unique_set_lte_cgi_15.add(line[10])
                                if len(cgi) == 16:
                                    lte_cgi_len16 += 1
                                    unique_set_lte_cgi_16.add(line[10])
                                if len(cgi) >= 17:
                                    lte_cgi_len17 += 1
                                    unique_set_lte_cgi_17.add(line[10])


                    if loc == 'WLS' or loc == '1':
                            loc = 'WLS'
                    elif loc == 'ECID' or loc == '2':
                            loc = 'ECID'
                    elif loc == 'CID' or loc == '3':
                            loc = 'CID'
                    elif loc == 'AGPS' or loc == '4':
                            loc = 'AGPS'
                    elif loc == 'HYBRID' or loc == '5':
                            loc = 'HYBRID'
                    elif loc == 'RWLS' or loc == '6':
                            loc = 'RWLS'
                    elif loc == 'OTHERS' or loc == '7':
                            loc = 'OTHERS'
                    elif loc == 'SWITCH' or loc == '8':
                            loc = 'SWITCH'
                    elif loc == 'PREDICTED' or loc == '9':
                            loc = 'PREDICTED'

                    total_records += 1
                    if carrier == "OM":
                        if imsi.startswith("42202"):
                            unique_set_imsi_om.add(line[0])
                            if msisdn == 'null' or msisdn == '':
                                if imei == 'null' or imei == '':
                                    unique_set_imsi_om_other_empty.add(line[0])

                        if imsi.startswith("42202") or imsi.startswith("42203"):
                            IMSI_Len_count_OMD(imsi)
                        if not imsi.startswith("42202") and not imsi.startswith("42203"):
                            IMSI_Len_count_OMF(imsi)

                    if carrier == "NW":
                        if imsi.startswith("42203"):
                            unique_set_imsi_or.add(line[0])
                            if msisdn == 'null' or msisdn == '':
                                if imei == 'null' or imei == '':
                                    unique_set_imsi_or_other_empty.add(line[0])

                        if imsi.startswith("42203") or imsi.startswith("42202"):
                            IMSI_Len_count_ORD(imsi)
                        if not imsi.startswith("42202") and not imsi.startswith("42203"):
                            IMSI_Len_count_ORF(imsi)
                    if not imsi.startswith("42202") and not imsi.startswith("42203"):
                        unique_set_foreign_imsi.add(line[0])
                        if msisdn == 'null' or msisdn == '':
                                if imei == 'null' or imei == '':
                                    unique_set_foreign_imsi_other_empty.add(line[0])

                    if msisdn == 'null' or msisdn == '':
                        pass
                    else:
                        if carrier == "OM":
                            if imsi.startswith("42202"):
                                imsi_msisdn_om_count +=1
                                MSISDN_Len_count_OMD(msisdn)
                                unique_set_msisdn_OM.add(line[0])
                            elif imsi.startswith("42203"):
                                domestic_roamer_or +=1
                                MSISDN_Len_count_ORD(msisdn)
                                unique_set_domestic_roamer_OR.add(line[0])
                            elif not imsi.startswith("42202") and not imsi.startswith("42203"):

                                foreign_imsi_with_msisdn_om +=1
                                MSISDN_Len_count_OMF(msisdn)
                                unique_set_msisdn_OM_FR.add(line[0])
                        if carrier == "NW":
                            if imsi.startswith("42203"):
                                imsi_msisdn_or_count +=1
                                MSISDN_Len_count_ORD(msisdn)
                                unique_set_msisdn_OR.add(line[0])
                            elif imsi.startswith("42202"):
                                domestic_roamer_om +=1
                                MSISDN_Len_count_OMD(msisdn)
                                unique_set_domestic_roamer_OM.add(line[0])
                            if not imsi.startswith("42202") and not imsi.startswith("42203"):
                                   foreign_imsi_with_msisdn_or +=1
                                   MSISDN_Len_count_ORF(msisdn)
#                                   unique_set_msisdn_OR_FR.add(line[0])
                                   unique_set_msisdn_OM_FR.add(line[0])
                        imsi_msisdn_count += 1
                        unique_set_msisdn.add(line[0])

                    if imei == 'null' or imei == '':
                        pass
                    else:
                        if carrier == "OM":
                            if imsi.startswith("42202"):
                                imsi_imei_om_count +=1
                                IMEI_Len_count_OMD(imei)
                                unique_set_imei_OM.add(line[0])
                            elif imsi.startswith("42203"):
                                imei_domestic_roamer_or +=1
                                IMEI_Len_count_ORD(imei)
                            elif not imsi.startswith("42202") and not imsi.startswith("42203"):
                                foreign_imsi_with_imei_om +=1
                                IMEI_Len_count_OMF(imei)
                                unique_set_imei_OM_FR.add(line[0])

                        if carrier == "NW":
                            if imsi.startswith("42203"):
                                imsi_imei_or_count +=1
                                IMEI_Len_count_ORD(imei)
                                unique_set_imei_OR.add(line[0])
                            elif imsi.startswith("42202"):
                                imei_domestic_roamer_om +=1
                                IMEI_Len_count_OMD(imei)
                            elif not imsi.startswith("42202") and not imsi.startswith("42203"):
                               foreign_imsi_with_imei_or +=1
                               IMEI_Len_count_ORF(imei)
#                               unique_set_imei_OR_FR.add(line[0])
                               unique_set_imei_OM_FR.add(line[0])
                        imsi_imei_count += 1
                        unique_set_imei.add(line[0])


                    if msisdn != 'null' and msisdn != '' and imei != 'null' and imei != '':
                        imsi_imei_msisdn_count +=1
                        unique_set_msisdn_imei.add(line[0])
                        if carrier == "OM":
                            if imsi.startswith("42202"):
                                imsi_imei_msisdn_om_count +=1
                                unique_set_msisdn_imei_OM.add(line[0])
                            elif imsi.startswith("42203"):
                                msisdn_imei_domestic_roamer_or +=1
                            elif not imsi.startswith("42202") and not imsi.startswith("42203"):
                                foreign_imsi_imei_msisdn_om +=1
                                unique_set_msisdn_imei_OM_FR.add(line[0])
                        if carrier == "NW":
                            if imsi.startswith("42203"):
                                imsi_imei_msisdn_or_count +=1
                                unique_set_msisdn_imei_OR.add(line[0])
                            elif imsi.startswith("42202"):
                                msisdn_imei_domestic_roamer_om +=1
                            elif not imsi.startswith("42202") and not imsi.startswith("42203"):
                               foreign_imsi_imei_msisdn_or +=1
#                               unique_set_msisdn_imei_OR_FR.add(line[0])
                               unique_set_msisdn_imei_OM_FR.add(line[0])

                        if carrier == "OM":

                            if imsi.startswith("42202"):
                                if event == 'MO SMS' and bparty != '' and bparty != 'null':
                                    mosms_bparty_omd += 1
                                if event == 'MT SMS' and bparty != '' and bparty != 'null':
                                    mtsms_bparty_omd += 1
                                if event == 'VOICE CALL START' and bparty != '' and bparty != 'null':
                                    vcs_bparty_omd += 1
                                if event == 'VOICE CALL END' and bparty != '' and bparty != 'null':
                                    vce_bparty_omd += 1
                            elif imsi.startswith("42203"):
                                if event == 'MO SMS' and bparty != '' and bparty != 'null':
                                    mosms_bparty_ominroamers += 1
                                if event == 'MT SMS' and bparty != '' and bparty != 'null':
                                    mtsms_bparty_ominroamers += 1
                                if event == 'VOICE CALL START' and bparty != '' and bparty != 'null':
                                    vcs_bparty_ominroamers += 1
                                if event == 'VOICE CALL END' and bparty != '' and bparty != 'null':
                                    vce_bparty_ominroamers += 1
                            elif not imsi.startswith("42202") and not imsi.startswith("42203"):
                                if event == 'MO SMS' and bparty != '' and bparty != 'null':
                                    mosms_bparty_omf += 1
                                if event == 'MT SMS' and bparty != '' and bparty != 'null':
                                    mtsms_bparty_omf += 1
                                if event == 'VOICE CALL START' and bparty != '' and bparty != 'null':
                                    vcs_bparty_omf += 1
                                if event == 'VOICE CALL END' and bparty != '' and bparty != 'null':
                                    vce_bparty_omf += 1

                        if carrier == "NW":
                            if imsi.startswith("42203"):
                                if event == 'MO SMS' and bparty != '' and bparty != 'null':
                                    mosms_bparty_ord += 1
                                if event == 'MT SMS' and bparty != '' and bparty != 'null':
                                    mtsms_bparty_ord += 1
                                if event == 'VOICE CALL START' and bparty != '' and bparty != 'null':
                                    vcs_bparty_ord += 1
                                if event == 'VOICE CALL END' and bparty != '' and bparty != 'null':
                                    vce_bparty_ord += 1
                            elif imsi.startswith("42202"):
                                if event == 'MO SMS' and bparty != '' and bparty != 'null':
                                    mosms_bparty_orinroamers += 1
                                if event == 'MT SMS' and bparty != '' and bparty != 'null':
                                    mtsms_bparty_orinroamers += 1
                                if event == 'VOICE CALL START' and bparty != '' and bparty != 'null':
                                    vcs_bparty_orinroamers += 1
                                if event == 'VOICE CALL END' and bparty != '' and bparty != 'null':
                                    vce_bparty_orinroamers += 1
                            elif not imsi.startswith("42202") and not imsi.startswith("42203"):
                                if event == 'MO SMS' and bparty != '' and bparty != 'null':
                                    mosms_bparty_orf += 1
                                if event == 'MT SMS' and bparty != '' and bparty != 'null':
                                    mtsms_bparty_orf += 1
                                if event == 'VOICE CALL START' and bparty != '' and bparty != 'null':
                                    vcs_bparty_orf += 1
                                if event == 'VOICE CALL END' and bparty != '' and bparty != 'null':
                                    vce_bparty_orf += 1

                        if event == 'VOICE CALL START':
                            total_vcs += 1
                        if event == 'VOICE CALL END':
                            total_vce += 1
                        if event == 'MT SMS':
                            total_mtsms += 1
                        if event == 'MO SMS':
                            total_mosms += 1
                        key1 = rat+'-'+loc+'-'+event
                        if key1 in kpidic:
                            value = kpidic[key1]
                            value += 1
                            kpidic[key1] = value


                with open(testPath+'/Mass-KPIs.txt','w') as newfile:
                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('          Total Records               '+'\n')
                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('Total records '+'= '+str(total_records)+'\n')
                    newfile.write('UNIQUE IMSIs with MSISDN '+'= '+str(len(unique_set_msisdn))+'\n')
                    newfile.write('UNIQUE IMSIs with IMEI '+'= '+str(len(unique_set_imei))+'\n')
                    newfile.write('UNIQUE IMSIS with both MSISDN and IMEI '+'= '+str(len(unique_set_msisdn_imei))+'\n')
                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('Total records with IMSI and MSISDN for OM and NW'+'= '+str(imsi_msisdn_count)+'\n')
                    newfile.write('OM Domestic Home '+'= '+str(imsi_msisdn_om_count)+'\t'+'\t' + 'NW Domestic Home  '+'= '+str(imsi_msisdn_or_count)+'\n')
                    newfile.write('OM Domestic Inroamers  '+'= '+str(domestic_roamer_om)+'\t' + 'NW Domestic Inroamers  '+'= '+str(domestic_roamer_or)+'\n')
                    newfile.write('OM Foreigners  '+'= '+str(foreign_imsi_with_msisdn_om)+'\t'+'\t' + 'NW Foreigners  '+'= '+str(foreign_imsi_with_msisdn_or)+'\n')
                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('Total records with IMSI and IMEI for OM and NW '+'= '+str(imsi_imei_count)+'\n')
                    newfile.write('OM Domestic Home '+'= '+str(imsi_imei_om_count)+'\t'+'\t' + 'NW DOmestic Home '+'= '+str(imsi_imei_or_count)+'\n')
                    newfile.write('OM Domestic Inroamers  '+'= '+str(imei_domestic_roamer_om)+'\t' + 'NW Domestic Inroamers  '+'= '+str(imei_domestic_roamer_om)+'\n')
                    newfile.write('OM Foreigners  '+'= '+str(foreign_imsi_with_imei_om)+'\t'+'\t' + 'NW Foreigners  '+'= '+str(foreign_imsi_with_imei_or)+'\n')
                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('Total records with IMSI, IMEI and MSISDN for OM and NW '+'= '+str(imsi_imei_msisdn_count)+'\n')
                    newfile.write('OM Domestic Home '+'= '+str(imsi_imei_msisdn_om_count)+'\t'+'\t' + 'NW Domestic Home '+'= '+str(imsi_imei_msisdn_or_count)+'\n')
                    newfile.write('OM Domestic Inroamers  '+'= '+str(msisdn_imei_domestic_roamer_om)+'\t' + 'NW Domestic Inroamers  '+'= '+str(msisdn_imei_domestic_roamer_or)+'\n')
                    newfile.write('OM Foreigners  '+'= '+str(foreign_imsi_imei_msisdn_om)+'\t'+'\t' + 'NW Foreigners  '+'= '+str(foreign_imsi_imei_msisdn_or)+'\n')

                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('    Domestic Omantel Subscribers          '+'\n')
                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('UNIQUE IMSIs  '+'= '+str(len(unique_set_imsi_om))+'\n')
                    newfile.write('UNIQUE IMSIs without MSISDN and IMEI  '+'= '+str(len(unique_set_imsi_om_other_empty))+'\n')
                    newfile.write('UNIQUE IMSIs with MSISDN  '+'= '+str(len(unique_set_msisdn_OM))+'\n')
                    newfile.write('UNIQUE IMSIs with IMEI  '+'= '+str(len(unique_set_imei_OM))+'\n')
                    newfile.write('UNIQUE IMSIs with both MSISDN and IMEI  '+'= '+str(len(unique_set_msisdn_imei_OM))+'\n')

                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('    Domestic Ooredoo Subscribers         '+'\n')
                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('UNIQUE IMSIs  '+'= '+str(len(unique_set_imsi_or))+'\n')
                    newfile.write('UNIQUE IMSIs without MSISDN and IMEI  '+'= '+str(len(unique_set_imsi_or_other_empty))+'\n')
                    newfile.write('UNIQUE IMSIs with MSISDN  '+'= '+str(len(unique_set_msisdn_OR))+'\n')
                    newfile.write('UNIQUE IMSIs with IMEI '+'= '+str(len(unique_set_imei_OR))+'\n')
                    newfile.write('UNIQUE IMSIs with both MSISDN and IMEI  '+'= '+str(len(unique_set_msisdn_imei_OR))+'\n')
                    newfile.write('\n')
                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('    Foreign Subscribers         '+'\n')
                    newfile.write('--------------------------------------'+'\n')
#                    newfile.write('Total IMSIs with MSISDN  '+'= '+str(foreign_imsi_with_msisdn_om)+'\n')
#                    newfile.write('Total IMSIs with IMEI  '+'= '+str(foreign_imsi_with_imei_om)+'\n')
#                    newfile.write('Total IMSIs with both MSISDN and IMEI '+'= '+str(foreign_imsi_imei_msisdn_om)+'\n')
                    newfile.write('UNIQUE IMSIs  '+'= '+str(len(unique_set_foreign_imsi))+'\n')
                    newfile.write('UNIQUE IMSIs without MSISDN and IMEI  '+'= '+str(len(unique_set_foreign_imsi_other_empty))+'\n')
                    newfile.write('UNIQUE IMSIs with MSISDN for OM and NW  '+'= '+str(len(unique_set_msisdn_OM_FR))+'\n')
                    newfile.write('UNIQUE IMSIs with IMEI for OM and NW  '+'= '+str(len(unique_set_imei_OM_FR))+'\n')
                    newfile.write('UNIQUE IMSIs with both MSISDN and IMEI for OM and NW '+'= '+str(len(unique_set_msisdn_imei_OM_FR))+'\n')
                    '''
                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('    Foreign Omantel Subscribers         '+'\n')
                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('UNIQUE IMSIs with MSISDN for OMANTEL '+'= '+str(len(unique_set_msisdn_OM_FR))+'\n')
                    newfile.write('UNIQUE IMSIs with IMEI for OMANTEL '+'= '+str(len(unique_set_imei_OM_FR))+'\n')
                    newfile.write('UNIQUE IMSIs with both MSISDN and IMEI for OMANTEL '+'= '+str(len(unique_set_msisdn_imei_OM_FR))+'\n')
                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('    Foreign Ooredoo Subscribers         '+'\n')
                    newfile.write('--------------------------------------'+'\n')
                    newfile.write('UNIQUE IMSIs with MSISDN for OOREDOO '+'= '+str(len(unique_set_msisdn_OR_FR))+'\n')
                    newfile.write('UNIQUE IMSIs with IMEI for OOREDOO '+'= '+str(len(unique_set_imei_OR_FR))+'\n')
                    newfile.write('UNIQUE IMSIs with both MSISDN and IMEI for OOREDOO '+'= '+str(len(unique_set_msisdn_imei_OR_FR))+'\n')
                    '''
                    newfile.write('\n')

                    newfile.write('1 digit Domestic IMSIs = OM -'+str(imsi_omd_len1)+'\t'+ 'NW -' +str(imsi_ord_len1)+'\n')
                    newfile.write('2 digit Domestic IMSIs = OM -'+str(imsi_omd_len2)+'\t'+ 'NW -'+str(imsi_ord_len2)+'\n')
                    newfile.write('3 digit Domestic IMSIs = OM -'+str(imsi_omd_len3)+'\t'+ 'NW -'+str(imsi_ord_len3)+'\n')
                    newfile.write('4 digit Domestic IMSIs = OM -'+str(imsi_omd_len4)+'\t'+ 'NW -'+str(imsi_ord_len4)+'\n')
                    newfile.write('5 digit Domestic IMSIs = OM -'+str(imsi_omd_len5)+'\t'+ 'NW -'+str(imsi_ord_len5)+'\n')
                    newfile.write('6 digit Domestic IMSIs = OM -'+str(imsi_omd_len6)+'\t'+ 'NW -'+str(imsi_ord_len6)+'\n')
                    newfile.write('7 digit Domestic IMSIs = OM -'+str(imsi_omd_len7)+'\t'+ 'NW -'+str(imsi_ord_len7)+'\n')
                    newfile.write('8 digit Domestic IMSIs = OM -'+str(imsi_omd_len8)+'\t'+ 'NW -'+str(imsi_ord_len8)+'\n')
                    newfile.write('9 digit Domestic IMSIs = OM -'+str(imsi_omd_len9)+'\t'+ 'NW -'+str(imsi_ord_len9)+'\n')
                    newfile.write('10 digit Domestic IMSIs = OM -'+str(imsi_omd_len10)+'\t'+ 'NW -'+str(imsi_ord_len10)+'\n')
                    newfile.write('11 digit Domestic IMSIs = OM -'+str(imsi_omd_len11)+'\t'+ 'NW -'+str(imsi_ord_len11)+'\n')
                    newfile.write('12 digit Domestic IMSIs = OM -'+str(imsi_omd_len12)+'\t'+ 'NW -'+str(imsi_ord_len12)+'\n')
                    newfile.write('13 digit Domestic IMSIs = OM -'+str(imsi_omd_len13)+'\t'+ 'NW -'+str(imsi_ord_len13)+'\n')
                    newfile.write('14 digit Domestic IMSIs = OM -'+str(imsi_omd_len14)+'\t'+ 'NW -'+str(imsi_ord_len14)+'\n')
                    newfile.write('15 digit Domestic IMSIs = OM -'+str(imsi_omd_len15)+'\t'+ 'NW -'+str(imsi_ord_len15)+'\n')
                    newfile.write('16 and greater than 16 digit Domestic IMSIs = OM -'+str(imsi_omd_len16)+'\t'+ 'NW -'+str(imsi_ord_len16)+'\n')
                    newfile.write('\n')
                    newfile.write('1 digit Foreign IMSIs = OM -'+str(imsi_omf_len1)+'\t'+ 'NW -' +str(imsi_orf_len1)+'\n')
                    newfile.write('2 digit Foreign IMSIs = OM -'+str(imsi_omf_len2)+'\t'+ 'NW -'+str(imsi_orf_len2)+'\n')
                    newfile.write('3 digit Foreign IMSIs = OM -'+str(imsi_omf_len3)+'\t'+ 'NW -'+str(imsi_orf_len3)+'\n')
                    newfile.write('4 digit Foreign IMSIs = OM -'+str(imsi_omf_len4)+'\t'+ 'NW -'+str(imsi_orf_len4)+'\n')
                    newfile.write('5 digit Foreign IMSIs = OM -'+str(imsi_omf_len5)+'\t'+ 'NW -'+str(imsi_orf_len5)+'\n')
                    newfile.write('6 digit Foreign IMSIs = OM -'+str(imsi_omf_len6)+'\t'+ 'NW -'+str(imsi_orf_len6)+'\n')
                    newfile.write('7 digit Foreign IMSIs = OM -'+str(imsi_omf_len7)+'\t'+ 'NW -'+str(imsi_orf_len7)+'\n')
                    newfile.write('8 digit Foreign IMSIs = OM -'+str(imsi_omf_len8)+'\t'+ 'NW -'+str(imsi_orf_len8)+'\n')
                    newfile.write('9 digit Foreign IMSIs = OM -'+str(imsi_omf_len9)+'\t'+ 'NW -'+str(imsi_orf_len9)+'\n')
                    newfile.write('10 digit Foreign IMSIs = OM -'+str(imsi_omf_len10)+'\t'+ 'NW -'+str(imsi_orf_len10)+'\n')
                    newfile.write('11 digit Foreign IMSIs = OM -'+str(imsi_omf_len11)+'\t'+ 'NW -'+str(imsi_orf_len11)+'\n')
                    newfile.write('12 digit Foreign IMSIs = OM -'+str(imsi_omf_len12)+'\t'+ 'NW -'+str(imsi_orf_len12)+'\n')
                    newfile.write('13 digit Foreign IMSIs = OM -'+str(imsi_omf_len13)+'\t'+ 'NW -'+str(imsi_orf_len13)+'\n')
                    newfile.write('14 digit Foreign IMSIs = OM -'+str(imsi_omf_len14)+'\t'+ 'NW -'+str(imsi_orf_len14)+'\n')
                    newfile.write('15 digit Foreign IMSIs = OM -'+str(imsi_omf_len15)+'\t'+ 'NW -'+str(imsi_orf_len15)+'\n')
                    newfile.write('16 and greater than 16 digit Foreign IMSIs = OM -'+str(imsi_omf_len16)+'\t'+ 'NW -'+str(imsi_orf_len16)+'\n')
                    newfile.write('\n')
                    newfile.write('1 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len1)+'\t'+ 'NW -'+str(msisdn_ord_len1)+'\n')
                    newfile.write('2 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len2)+'\t'+ 'NW -'+str(msisdn_ord_len2)+'\n')
                    newfile.write('3 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len3)+'\t'+ 'NW -'+str(msisdn_ord_len3)+'\n')
                    newfile.write('4 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len4)+'\t'+ 'NW -'+str(msisdn_ord_len4)+'\n')
                    newfile.write('5 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len5)+'\t'+ 'NW -'+str(msisdn_ord_len5)+'\n')
                    newfile.write('6 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len6)+'\t'+ 'NW -'+str(msisdn_ord_len6)+'\n')
                    newfile.write('7 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len7)+'\t'+ 'NW -'+str(msisdn_ord_len7)+'\n')
                    newfile.write('8 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len8)+'\t'+ 'NW -'+str(msisdn_ord_len8)+'\n')
                    newfile.write('9 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len9)+'\t'+ 'NW -'+str(msisdn_ord_len9)+'\n')
                    newfile.write('10 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len10)+'\t'+ 'NW -'+str(msisdn_ord_len10)+'\n')
                    newfile.write('11 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len11)+'\t'+ 'NW -'+str(msisdn_ord_len11)+'\n')
                    newfile.write('12 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len12)+'\t'+ 'NW -'+str(msisdn_ord_len12)+'\n')
                    newfile.write('13 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len13)+'\t'+ 'NW -'+str(msisdn_ord_len13)+'\n')
                    newfile.write('14 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len14)+'\t'+ 'NW -'+str(msisdn_ord_len14)+'\n')
                    newfile.write('15 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len15)+'\t'+ 'NW -'+str(msisdn_ord_len15)+'\n')
                    newfile.write('16 and greater than 16 digit Domestic MSISDNs = OM -'+str(msisdn_omd_len16)+'\t'+ 'NW -'+str(msisdn_ord_len16)+'\n')
                    newfile.write('\n')
                    newfile.write('1 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len1)+'\t'+ 'NW -'+str(msisdn_orf_len1)+'\n')
                    newfile.write('2 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len2)+'\t'+ 'NW -'+str(msisdn_orf_len2)+'\n')
                    newfile.write('3 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len3)+'\t'+ 'NW -'+str(msisdn_orf_len3)+'\n')
                    newfile.write('4 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len4)+'\t'+ 'NW -'+str(msisdn_orf_len4)+'\n')
                    newfile.write('5 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len5)+'\t'+ 'NW -'+str(msisdn_orf_len5)+'\n')
                    newfile.write('6 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len6)+'\t'+ 'NW -'+str(msisdn_orf_len6)+'\n')
                    newfile.write('7 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len7)+'\t'+'\t'+ 'NW -'+str(msisdn_orf_len7)+'\n')
                    newfile.write('8 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len8)+'\t'+'\t'+ 'NW -'+str(msisdn_orf_len8)+'\n')
                    newfile.write('9 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len9)+'\t'+'\t'+ 'NW -'+str(msisdn_orf_len9)+'\n')
                    newfile.write('10 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len10)+'\t'+ 'NW -'+str(msisdn_orf_len10)+'\n')
                    newfile.write('11 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len11)+'\t'+ 'NW -'+str(msisdn_orf_len11)+'\n')
                    newfile.write('12 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len12)+'\t'+ 'NW -'+str(msisdn_orf_len12)+'\n')
                    newfile.write('13 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len13)+'\t'+ 'NW -'+str(msisdn_orf_len13)+'\n')
                    newfile.write('14 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len14)+'\t'+ 'NW -'+str(msisdn_orf_len14)+'\n')
                    newfile.write('15 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len15)+'\t'+ 'NW -'+str(msisdn_orf_len15)+'\n')
                    newfile.write('16 and greater than 16 digit Foreign MSISDNs = OM -'+str(msisdn_omf_len16)+'\t'+ 'NW -'+str(msisdn_orf_len16)+'\n')
                    newfile.write('\n')
                    newfile.write('1 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len1)+'\t'+ 'NW -'+str(imei_ord_len1)+'\n')
                    newfile.write('2 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len2)+'\t'+ 'NW -'+str(imei_ord_len2)+'\n')
                    newfile.write('3 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len3)+'\t'+ 'NW -'+str(imei_ord_len3)+'\n')
                    newfile.write('4 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len4)+'\t'+ 'NW -'+str(imei_ord_len4)+'\n')
                    newfile.write('5 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len5)+'\t'+ 'NW -'+str(imei_ord_len5)+'\n')
                    newfile.write('6 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len6)+'\t'+ 'NW -'+str(imei_ord_len6)+'\n')
                    newfile.write('7 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len7)+'\t'+ 'NW -'+str(imei_ord_len7)+'\n')
                    newfile.write('8 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len8)+'\t'+ 'NW -'+str(imei_ord_len8)+'\n')
                    newfile.write('9 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len9)+'\t'+ 'NW -'+str(imei_ord_len9)+'\n')
                    newfile.write('10 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len10)+'\t'+ 'NW -'+str(imei_ord_len10)+'\n')
                    newfile.write('11 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len11)+'\t'+ 'NW -'+str(imei_ord_len11)+'\n')
                    newfile.write('12 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len12)+'\t'+ 'NW -'+str(imei_ord_len12)+'\n')
                    newfile.write('13 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len13)+'\t'+ 'NW -'+str(imei_ord_len13)+'\n')
                    newfile.write('14 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len14)+'\t'+ 'NW -'+str(imei_ord_len14)+'\n')
                    newfile.write('15 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len15)+'\t'+ 'NW -'+str(imei_ord_len15)+'\n')
                    newfile.write('16 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len16)+'\t'+ 'NW -'+str(imei_ord_len16)+'\n')
                    newfile.write('17 and greater than 17 digit Domestic IMEIs '+'= OM -'+str(imei_omd_len17)+'\t'+ 'NW -'+str(imei_ord_len17)+'\n')
                    newfile.write('\n')
                    newfile.write('1 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len1)+'\t'+ 'NW -'+str(imei_orf_len1)+'\n')
                    newfile.write('2 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len2)+'\t'+ 'NW -'+str(imei_orf_len2)+'\n')
                    newfile.write('3 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len3)+'\t'+ 'NW -'+str(imei_orf_len3)+'\n')
                    newfile.write('4 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len4)+'\t'+ 'NW -'+str(imei_orf_len4)+'\n')
                    newfile.write('5 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len5)+'\t'+ 'NW -'+str(imei_orf_len5)+'\n')
                    newfile.write('6 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len6)+'\t'+ 'NW -'+str(imei_orf_len6)+'\n')
                    newfile.write('7 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len7)+'\t'+ 'NW -'+str(imei_orf_len7)+'\n')
                    newfile.write('8 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len8)+'\t'+ 'NW -'+str(imei_orf_len8)+'\n')
                    newfile.write('9 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len9)+'\t'+ 'NW -'+str(imei_orf_len9)+'\n')
                    newfile.write('10 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len10)+'\t'+ 'NW -'+str(imei_orf_len10)+'\n')
                    newfile.write('11 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len11)+'\t'+ 'NW -'+str(imei_orf_len11)+'\n')
                    newfile.write('12 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len12)+'\t'+ 'NW -'+str(imei_orf_len12)+'\n')
                    newfile.write('13 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len13)+'\t'+ 'NW -'+str(imei_orf_len13)+'\n')
                    newfile.write('14 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len14)+'\t'+ 'NW -'+str(imei_orf_len14)+'\n')
                    newfile.write('15 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len15)+'\t'+ 'NW -'+str(imei_orf_len15)+'\n')
                    newfile.write('16 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len16)+'\t'+ 'NW -'+str(imei_orf_len16)+'\n')
                    newfile.write('17 and greater than 17 digit Foreign IMEIs '+'= OM -'+str(imei_omf_len17)+'\t'+ 'NW -'+str(imei_orf_len17)+'\n')
                    newfile.write('\n')
                    newfile.write('1 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len1)+'\t'+'UMTS'+'='+str(umts_cgi_len1)+'\t'+'LTE'+'='+str(lte_cgi_len1)+'\n')
                    newfile.write('2 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len2)+'\t'+'UMTS'+'='+str(umts_cgi_len2)+'\t'+'LTE'+'='+str(lte_cgi_len2)+'\n')
                    newfile.write('3 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len3)+'\t'+'UMTS'+'='+str(umts_cgi_len3)+'\t'+'LTE'+'='+str(lte_cgi_len3)+'\n')
                    newfile.write('4 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len4)+'\t'+'UMTS'+'='+str(umts_cgi_len4)+'\t'+'LTE'+'='+str(lte_cgi_len4)+'\n')
                    newfile.write('5 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len5)+'\t'+'UMTS'+'='+str(umts_cgi_len5)+'\t'+'LTE'+'='+str(lte_cgi_len5)+'\n')
                    newfile.write('6 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len6)+'\t'+'UMTS'+'='+str(umts_cgi_len6)+'\t'+'LTE'+'='+str(lte_cgi_len6)+'\n')
                    newfile.write('7 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len7)+'\t'+'UMTS'+'='+str(umts_cgi_len7)+'\t'+'LTE'+'='+str(lte_cgi_len7)+'\n')
                    newfile.write('8 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len8)+'\t'+'UMTS'+'='+str(umts_cgi_len8)+'\t'+'LTE'+'='+str(lte_cgi_len8)+'\n')
                    newfile.write('9 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len9)+'\t'+'UMTS'+'='+str(umts_cgi_len9)+'\t'+'LTE'+'='+str(lte_cgi_len9)+'\n')
                    newfile.write('10 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len10)+'\t'+'UMTS'+'='+str(umts_cgi_len10)+'\t'+'LTE'+'='+str(lte_cgi_len10)+'\n')
                    newfile.write('11 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len11)+'\t'+'UMTS'+'='+str(umts_cgi_len11)+'\t'+'LTE'+'='+str(lte_cgi_len11)+'\n')
                    newfile.write('12 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len12)+'\t'+'UMTS'+'='+str(umts_cgi_len12)+'\t'+'LTE'+'='+str(lte_cgi_len12)+'\n')
                    newfile.write('13 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len13)+'\t'+'UMTS'+'='+str(umts_cgi_len13)+'\t'+'LTE'+'='+str(lte_cgi_len13)+'\n')
                    newfile.write('14 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len14)+'\t'+'UMTS'+'='+str(umts_cgi_len14)+'\t'+'LTE'+'='+str(lte_cgi_len14)+'\n')
                    newfile.write('15 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len15)+'\t'+'UMTS'+'='+str(umts_cgi_len15)+'\t'+'LTE'+'='+str(lte_cgi_len15)+'\n')
                    newfile.write('16 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len16)+'\t'+'UMTS'+'='+str(umts_cgi_len16)+'\t'+'LTE'+'='+str(lte_cgi_len16)+'\n')
                    newfile.write('17 and greater than 17 digit CGI'+'---->'+'GSM'+'='+str(gsm_cgi_len17)+'\t'+'UMTS'+'='+str(umts_cgi_len17)+'\t'+'LTE'+'='+str(lte_cgi_len17)+'\n')
                    newfile.write('\n')
                    newfile.write('1 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_1))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_1))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_1))+'\n')
                    newfile.write('2 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_2))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_2))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_2))+'\n')
                    newfile.write('3 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_3))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_3))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_3))+'\n')
                    newfile.write('4 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_4))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_4))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_4))+'\n')
                    newfile.write('5 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_5))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_5))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_5))+'\n')
                    newfile.write('6 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_6))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_6))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_6))+'\n')
                    newfile.write('7 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_7))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_7))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_7))+'\n')
                    newfile.write('8 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_8))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_8))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_8))+'\n')
                    newfile.write('9 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_9))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_9))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_9))+'\n')
                    newfile.write('10 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_10))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_10))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_10))+'\n')
                    newfile.write('11 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_11))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_11))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_11))+'\n')
                    newfile.write('12 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_12))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_12))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_12))+'\n')
                    newfile.write('13 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_13))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_13))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_13))+'\n')
                    newfile.write('14 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_14))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_14))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_14))+'\n')
                    newfile.write('15 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_15))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_15))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_15))+'\n')
                    newfile.write('16 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_16))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_16))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_16))+'\n')
                    newfile.write('17 and greater than 17 digit UNIQUE CGI'+'---->'+'GSM'+'='+str(len(unique_set_gsm_cgi_17))+'\t'+'UMTS'+'='+str(len(unique_set_umts_cgi_17))+'\t'+'LTE'+'='+str(len(unique_set_lte_cgi_17))+'\n')
                    newfile.write('\n')
                    newfile.write('Total MOSMS events for OM and NW '+'= '+str(total_mosms)+'\n')
                    newfile.write('Total MTSMS events for OM and NW '+'= '+str(total_mtsms)+'\n')
                    newfile.write('Total VOICECALLSTART events for OM and NW'+'= '+str(total_vcs)+'\n')
                    newfile.write('Total VOICECALLEND events for OM and NW'+'= '+str(total_vce)+'\n')
                    newfile.write('------------------------------------------------------'+'\n')
                    newfile.write('  MOSMS events with bparty number '+'\n')
                    newfile.write('------------------------------------------------------'+'\n')
                    newfile.write('OM MOSMS Domestic Home '+'= '+str(mosms_bparty_omd)+'\t'+'\t' + 'NW MOSMS Domestic Home  '+'= '+str(mosms_bparty_ord)+'\n')
                    newfile.write('OM MOSMS Domestic Inroamers  '+'= '+str(mosms_bparty_ominroamers)+'\t' + 'NW MOSMS Domestic Inroamers  '+'= '+str(mosms_bparty_orinroamers)+'\n')
                    newfile.write('OM MOSMS Foreigners  '+'= '+str(mosms_bparty_omf)+'\t'+'\t' + 'NW MOSMS Foreigners  '+'= '+str(mosms_bparty_orf)+'\n')
                    newfile.write('-------------------------------------------------------'+'\n')
                    newfile.write('  MTSMS events with bparty number '+'\n')
                    newfile.write('-------------------------------------------------------'+'\n')
                    newfile.write('OM MTSMS Domestic Home '+'= '+str(mtsms_bparty_omd)+'\t'+'\t' + 'NW MTSMS Domestic Home  '+'= '+str(mtsms_bparty_ord)+'\n')
                    newfile.write('OM MTSMS Domestic Inroamers  '+'= '+str(mtsms_bparty_ominroamers)+'\t' + 'NW MTSMS Domestic Inroamers  '+'= '+str(mtsms_bparty_orinroamers)+'\n')
                    newfile.write('OM MTSMS Foreigners  '+'= '+str(mtsms_bparty_omf)+'\t'+'\t' + 'NW MTSMS Foreigners  '+'= '+str(mtsms_bparty_orf)+'\n')
                    newfile.write('-------------------------------------------------------'+'\n')
                    newfile.write('  VOICE CALL START events with bparty number '+'\n')
                    newfile.write('-------------------------------------------------------'+'\n')
                    newfile.write('OM VOICE CALL START Domestic Home '+'= '+str(vcs_bparty_omd)+'\t'+'\t' + 'NW VOICE CALL START Domestic Home  '+'= '+str(vcs_bparty_ord)+'\n')
                    newfile.write('OM VOICE CALL START Domestic Inroamers  '+'= '+str(vcs_bparty_ominroamers)+'\t' + 'NW VOICE CALL START Domestic Inroamers  '+'= '+str(vcs_bparty_orinroamers)+'\n')
                    newfile.write('OM VOICE CALL START Foreigners  '+'= '+str(vcs_bparty_omf)+'\t'+'\t' + 'NW VOICE CALL START Foreigners  '+'= '+str(vcs_bparty_orf)+'\n')
                    newfile.write('-------------------------------------------------------'+'\n')
                    newfile.write('  VOICE CALL END events with bparty number '+'\n')
                    newfile.write('-------------------------------------------------------'+'\n')
                    newfile.write('OM VOICE CALL END Domestic Home '+'= '+str(vce_bparty_omd)+'\t'+'\t' + 'NW VOICE CALL END Domestic Home  '+'= '+str(vce_bparty_ord)+'\n')
                    newfile.write('OM VOICE CALL END Domestic Inroamers  '+'= '+str(vce_bparty_ominroamers)+'\t' + 'NW VOICE CALL END Domestic Inroamers  '+'= '+str(vce_bparty_orinroamers)+'\n')
                    newfile.write('OM VOICE CALL END Foreigners  '+'= '+str(vce_bparty_omf)+'\t'+'\t' + 'NW VOICE CALL END Foreigners  '+'= '+str(vce_bparty_orf)+'\n')


def IMSI_Len_count_OMD(imsi):
    global imsi_omd_len1;global imsi_omd_len2;global imsi_omd_len3;global imsi_omd_len4;global imsi_omd_len5;global imsi_omd_len6;global imsi_omd_len7;global imsi_omd_len8;global imsi_omd_len9;global imsi_omd_len10;global imsi_omd_len11;global imsi_omd_len12;global imsi_omd_len13;global imsi_omd_len14;global imsi_omd_len15;global imsi_omd_len16
    if len(imsi) == 0:
        pass
    elif len(imsi) == 1:
        imsi_omd_len1 += 1
    elif len(imsi) == 2:
        imsi_omd_len2 += 1
    elif len(imsi) == 3:
        imsi_omd_len3 += 1
    elif len(imsi) == 4:
        imsi_omd_len4 += 1
    elif len(imsi) == 5:
        imsi_omd_len5 += 1
    elif len(imsi) == 6:
        imsi_omd_len6 += 1
    elif len(imsi) == 7:
        imsi_omd_len7 += 1
    elif len(imsi) == 8:
        imsi_omd_len8 += 1
    elif len(imsi) == 9:
        imsi_omd_len9 += 1
    elif len(imsi) == 10:
        imsi_omd_len10 += 1
    elif len(imsi) == 11:
        imsi_omd_len11 += 1
    elif len(imsi) == 12:
        imsi_omd_len12 += 1
    elif len(imsi) == 13:
        imsi_omd_len13 += 1
    elif len(imsi) == 14:
        imsi_omd_len14 += 1
    elif len(imsi) == 15:
        imsi_omd_len15 += 1
    elif len(imsi) >= 16:
        imsi_omd_len16 += 1

def IMSI_Len_count_ORD(imsi):
        global imsi_ord_len1;global imsi_ord_len2;global imsi_ord_len3;global imsi_ord_len4;global imsi_ord_len5;global imsi_ord_len6;global imsi_ord_len7;global imsi_ord_len8;global imsi_ord_len9;global imsi_ord_len10;global imsi_ord_len11;global imsi_ord_len12;global imsi_ord_len13;global imsi_ord_len14;global imsi_ord_len15;global imsi_ord_len16
        if len(imsi) == 0:
                pass
        elif len(imsi) == 1:
                imsi_ord_len1 += 1
        elif len(imsi) == 2:
                imsi_ord_len2 += 1
        elif len(imsi) == 3:
                imsi_ord_len3 += 1
        elif len(imsi) == 4:
                imsi_ord_len4 += 1
        elif len(imsi) == 5:
                imsi_ord_len5 += 1
        elif len(imsi) == 6:
                imsi_ord_len6 += 1
        elif len(imsi) == 7:
                imsi_ord_len7 += 1
        elif len(imsi) == 8:
                imsi_ord_len8 += 1
        elif len(imsi) == 9:
                imsi_ord_len9 += 1
        elif len(imsi) == 10:
                imsi_ord_len10 += 1
        elif len(imsi) == 11:
                imsi_ord_len11 += 1
        elif len(imsi) == 12:
                imsi_ord_len12 += 1
        elif len(imsi) == 13:
                imsi_ord_len13 += 1
        elif len(imsi) == 14:
                imsi_ord_len14 += 1
        elif len(imsi) == 15:
                imsi_ord_len15 += 1
        elif len(imsi) >= 16:
                imsi_ord_len16 += 1

def IMSI_Len_count_OMF(imsi):
        global imsi_omf_len1;global imsi_omf_len2;global imsi_omf_len3;global imsi_omf_len4;global imsi_omf_len5;global imsi_omf_len6;global imsi_omf_len7;global imsi_omf_len8;global imsi_omf_len9;global imsi_omf_len10;global imsi_omf_len11;global imsi_omf_len12;global imsi_omf_len13;global imsi_omf_len14;global imsi_omf_len15;global imsi_omf_len16
        if len(imsi) == 0:
                pass
        elif len(imsi) == 1:
                imsi_omf_len1 += 1
        elif len(imsi) == 2:
                imsi_omf_len2 += 1
        elif len(imsi) == 3:
                imsi_omf_len3 += 1
        elif len(imsi) == 4:
                imsi_omf_len4 += 1
        elif len(imsi) == 5:
                imsi_omf_len5 += 1
        elif len(imsi) == 6:
                imsi_omf_len6 += 1
        elif len(imsi) == 7:
                imsi_omf_len7 += 1
        elif len(imsi) == 8:
                imsi_omf_len8 += 1
        elif len(imsi) == 9:
                imsi_omf_len9 += 1
        elif len(imsi) == 10:
                imsi_omf_len10 += 1
        elif len(imsi) == 11:
                imsi_omf_len11 += 1
        elif len(imsi) == 12:
                imsi_omf_len12 += 1
        elif len(imsi) == 13:
                imsi_omf_len13 += 1
        elif len(imsi) == 14:
                imsi_omf_len14 += 1
        elif len(imsi) == 15:
                imsi_omf_len15 += 1
        elif len(imsi) == 16:
                imsi_omf_len16 += 1

def IMSI_Len_count_ORF(imsi):
        global imsi_orf_len1;global imsi_orf_len2;global imsi_orf_len3;global imsi_orf_len4;global imsi_orf_len5;global imsi_orf_len6;global imsi_orf_len7;global imsi_orf_len8;global imsi_orf_len9;global imsi_orf_len10;global imsi_orf_len11;global imsi_orf_len12;global imsi_orf_len13;global imsi_orf_len14;global imsi_orf_len15;global imsi_orf_len16
        if len(imsi) == 0:
                pass
        elif len(imsi) == 1:
                imsi_orf_len1 += 1
        elif len(imsi) == 2:
                imsi_orf_len2 += 1
        elif len(imsi) == 3:
                imsi_orf_len3 += 1
        elif len(imsi) == 4:
                imsi_orf_len4 += 1
        elif len(imsi) == 5:
                imsi_orf_len5 += 1
        elif len(imsi) == 6:
                imsi_orf_len6 += 1
        elif len(imsi) == 7:
                imsi_orf_len7 += 1
        elif len(imsi) == 8:
                imsi_orf_len8 += 1
        elif len(imsi) == 9:
                imsi_orf_len9 += 1
        elif len(imsi) == 10:
                imsi_orf_len10 += 1
        elif len(imsi) == 11:
                imsi_orf_len11 += 1
        elif len(imsi) == 12:
                imsi_orf_len12 += 1
        elif len(imsi) == 13:
                imsi_orf_len13 += 1
        elif len(imsi) == 14:
                imsi_orf_len14 += 1
        elif len(imsi) == 15:
                imsi_orf_len15 += 1
        elif len(imsi) == 16:
                imsi_orf_len16 += 1
def MSISDN_Len_count_OMD(msisdn):
        global msisdn_omd_len1;global msisdn_omd_len2;global msisdn_omd_len3;global msisdn_omd_len4;global msisdn_omd_len5;global msisdn_omd_len6;global msisdn_omd_len7;global msisdn_omd_len8;global msisdn_omd_len9;global msisdn_omd_len10;global msisdn_omd_len11;global msisdn_omd_len12;global msisdn_omd_len13;global msisdn_omd_len14;global msisdn_omd_len15;global msisdn_omd_len16
        if len(msisdn) == 0:
                pass
        elif len(msisdn) == 1:
            msisdn_omd_len1 += 1
        elif len(msisdn) == 2:
            msisdn_omd_len2 += 1
        elif len(msisdn) == 3:
            msisdn_omd_len3 += 1
        elif len(msisdn) == 4:
            msisdn_omd_len4 += 1
        elif len(msisdn) == 5:
            msisdn_omd_len5 += 1
        elif len(msisdn) == 6:
            msisdn_omd_len6 += 1
        elif len(msisdn) == 7:
            msisdn_omd_len7 += 1
        elif len(msisdn) == 8:
            msisdn_omd_len8 += 1
        elif len(msisdn) == 9:
            msisdn_omd_len9 += 1
        elif len(msisdn) == 10:
            msisdn_omd_len10 += 1
        elif len(msisdn) == 11:
            msisdn_omd_len11 += 1
        elif len(msisdn) == 12:
            msisdn_omd_len12 += 1
        elif len(msisdn) == 13:
            msisdn_omd_len13 += 1
        elif len(msisdn) == 14:
            msisdn_omd_len14 += 1
        elif len(msisdn) == 15:
            msisdn_omd_len15 += 1
        elif len(msisdn) >= 16:
            msisdn_omd_len16 += 1

def MSISDN_Len_count_ORD(msisdn):
        global msisdn_ord_len1;global msisdn_ord_len2;global msisdn_ord_len3;global msisdn_ord_len4;global msisdn_ord_len5;global msisdn_ord_len6;global msisdn_ord_len7;global msisdn_ord_len8;global msisdn_ord_len9;global msisdn_ord_len10;global msisdn_ord_len11;global msisdn_ord_len12;global msisdn_ord_len13;global msisdn_ord_len14;global msisdn_ord_len15;global msisdn_ord_len16
        if len(msisdn) == 0:
                pass
        elif len(msisdn) == 1:
            msisdn_ord_len1 += 1
        elif len(msisdn) == 2:
            msisdn_ord_len2 += 1
        elif len(msisdn) == 3:
            msisdn_ord_len3 += 1
        elif len(msisdn) == 4:
            msisdn_ord_len4 += 1
        elif len(msisdn) == 5:
            msisdn_ord_len5 += 1
        elif len(msisdn) == 6:
            msisdn_ord_len6 += 1
        elif len(msisdn) == 7:
            msisdn_ord_len7 += 1
        elif len(msisdn) == 8:
            msisdn_ord_len8 += 1
        elif len(msisdn) == 9:
            msisdn_ord_len9 += 1
        elif len(msisdn) == 10:
            msisdn_ord_len10 += 1
        elif len(msisdn) == 11:
            msisdn_ord_len11 += 1
        elif len(msisdn) == 12:
            msisdn_ord_len12 += 1
        elif len(msisdn) == 13:
            msisdn_ord_len13 += 1
        elif len(msisdn) == 14:
            msisdn_ord_len14 += 1
        elif len(msisdn) == 15:
            msisdn_ord_len15 += 1
        elif len(msisdn) >= 16:
            msisdn_ord_len16 += 1

def MSISDN_Len_count_OMF(msisdn):
        global msisdn_omf_len1;global msisdn_omf_len2;global msisdn_omf_len3;global msisdn_omf_len4;global msisdn_omf_len5;global msisdn_omf_len6;global msisdn_omf_len7;global msisdn_omf_len8;global msisdn_omf_len9;global msisdn_omf_len10;global msisdn_omf_len11;global msisdn_omf_len12;global msisdn_omf_len13;global msisdn_omf_len14;global msisdn_omf_len15;global msisdn_omf_len16
        if len(msisdn) == 0:
                pass
        elif len(msisdn) == 1:
            msisdn_omf_len1 += 1
        elif len(msisdn) == 2:
            msisdn_omf_len2 += 1
        elif len(msisdn) == 3:
            msisdn_omf_len3 += 1
        elif len(msisdn) == 4:
            msisdn_omf_len4 += 1
        elif len(msisdn) == 5:
            msisdn_omf_len5 += 1
        elif len(msisdn) == 6:
            msisdn_omf_len6 += 1
        elif len(msisdn) == 7:
            msisdn_omf_len7 += 1
        elif len(msisdn) == 8:
            msisdn_omf_len8 += 1
        elif len(msisdn) == 9:
            msisdn_omf_len9 += 1
        elif len(msisdn) == 10:
            msisdn_omf_len10 += 1
        elif len(msisdn) == 11:
            msisdn_omf_len11 += 1
        elif len(msisdn) == 12:
            msisdn_omf_len12 += 1
        elif len(msisdn) == 13:
            msisdn_omf_len13 += 1
        elif len(msisdn) == 14:
            msisdn_omf_len14 += 1
        elif len(msisdn) == 15:
            msisdn_omf_len15 += 1
        elif len(msisdn) >= 16:
            msisdn_omf_len16 += 1

def MSISDN_Len_count_ORF(msisdn):
        global msisdn_orf_len1;global msisdn_orf_len2;global msisdn_orf_len3;global msisdn_orf_len4;global msisdn_orf_len5;global msisdn_orf_len6;global msisdn_orf_len7;global msisdn_orf_len8;global msisdn_orf_len9;global msisdn_orf_len10;global msisdn_orf_len11;global msisdn_orf_len12;global msisdn_orf_len13;global msisdn_orf_len14;global msisdn_orf_len15;global msisdn_orf_len16
        if len(msisdn) == 0:
                pass
        elif len(msisdn) == 1:
            msisdn_orf_len1 += 1
        elif len(msisdn) == 2:
            msisdn_orf_len2 += 1
        elif len(msisdn) == 3:
            msisdn_orf_len3 += 1
        elif len(msisdn) == 4:
            msisdn_orf_len4 += 1
        elif len(msisdn) == 5:
            msisdn_orf_len5 += 1
        elif len(msisdn) == 6:
            msisdn_orf_len6 += 1
        elif len(msisdn) == 7:
            msisdn_orf_len7 += 1
        elif len(msisdn) == 8:
            msisdn_orf_len8 += 1
        elif len(msisdn) == 9:
            msisdn_orf_len9 += 1
        elif len(msisdn) == 10:
            msisdn_orf_len10 += 1
        elif len(msisdn) == 11:
            msisdn_orf_len11 += 1
        elif len(msisdn) == 12:
            msisdn_orf_len12 += 1
        elif len(msisdn) == 13:
            msisdn_orf_len13 += 1
        elif len(msisdn) == 14:
            msisdn_orf_len14 += 1
        elif len(msisdn) == 15:
            msisdn_orf_len15 += 1
        elif len(msisdn) >= 16:
            msisdn_orf_len16 += 1

def IMEI_Len_count_OMD(imei):
    global imei_omd_len1;global imei_omd_len2;global imei_omd_len3;global imei_omd_len4;global imei_omd_len5;global imei_omd_len6;global imei_omd_len7;global imei_omd_len8;global imei_omd_len9;global imei_omd_len10;global imei_omd_len11;global imei_omd_len12;global imei_omd_len13;global imei_omd_len14;global imei_omd_len15;global imei_omd_len16;global imei_omd_len17
    if len(imei) == 0:
        pass
    elif len(imei) == 1:
        imei_omd_len1 += 1
    elif len(imei) == 2:
        imei_omd_len2 += 1
    elif len(imei) == 3:
        imei_omd_len3 += 1
    elif len(imei) == 4:
        imei_omd_len4 += 1
    elif len(imei) == 5:
        imei_omd_len5 += 1
    elif len(imei) == 6:
        imei_omd_len6 += 1
    elif len(imei) == 7:
        imei_omd_len7 += 1
    elif len(imei) == 8:
        imei_omd_len8 += 1
    elif len(imei) == 9:
        imei_omd_len9 += 1
    elif len(imei) == 10:
        imei_omd_len10 += 1
    elif len(imei) == 11:
        imei_omd_len11 += 1
    elif len(imei) == 12:
        imei_omd_len12 += 1
    elif len(imei) == 13:
        imei_omd_len13 += 1
    elif len(imei) == 14:
        imei_omd_len14 += 1
    elif len(imei) == 15:
        imei_omd_len15 += 1
    elif len(imei) == 16:
        imei_omd_len16 += 1
    elif len(imei) >= 17:
        imei_omd_len17 += 1

def IMEI_Len_count_ORD(imei):
    global imei_ord_len1;global imei_ord_len2;global imei_ord_len3;global imei_ord_len4;global imei_ord_len5;global imei_ord_len6;global imei_ord_len7;global imei_ord_len8;global imei_ord_len9;global imei_ord_len10;global imei_ord_len11;global imei_ord_len12;global imei_ord_len13;global imei_ord_len14;global imei_ord_len15;global imei_ord_len16;global imei_ord_len17
    if len(imei) == 0:
        pass
    elif len(imei) == 1:
        imei_ord_len1 += 1
    elif len(imei) == 2:
        imei_ord_len2 += 1
    elif len(imei) == 3:
        imei_ord_len3 += 1
    elif len(imei) == 4:
        imei_ord_len4 += 1
    elif len(imei) == 5:
        imei_ord_len5 += 1
    elif len(imei) == 6:
        imei_ord_len6 += 1
    elif len(imei) == 7:
        imei_ord_len7 += 1
    elif len(imei) == 8:
        imei_ord_len8 += 1
    elif len(imei) == 9:
        imei_ord_len9 += 1
    elif len(imei) == 10:
        imei_ord_len10 += 1
    elif len(imei) == 11:
        imei_ord_len11 += 1
    elif len(imei) == 12:
        imei_ord_len12 += 1
    elif len(imei) == 13:
        imei_ord_len13 += 1
    elif len(imei) == 14:
        imei_ord_len14 += 1
    elif len(imei) == 15:
        imei_ord_len15 += 1
    elif len(imei) == 16:
        imei_ord_len16 += 1
    elif len(imei) >= 17:
        imei_ord_len17 += 1

def IMEI_Len_count_OMF(imei):
    global imei_omf_len1;global imei_omf_len2;global imei_omf_len3;global imei_omf_len4;global imei_omf_len5;global imei_omf_len6;global imei_omf_len7;global imei_omf_len8;global imei_omf_len9;global imei_omf_len10;global imei_omf_len11;global imei_omf_len17;global imei_omf_len12;global imei_omf_len13;global imei_omf_len14;global imei_omf_len15;global imei_omf_len16
    if len(imei) == 0:
        pass
    elif len(imei) == 1:
        imei_omf_len1 += 1
    elif len(imei) == 2:
        imei_omf_len2 += 1
    elif len(imei) == 3:
        imei_omf_len3 += 1
    elif len(imei) == 4:
        imei_omf_len4 += 1
    elif len(imei) == 5:
        imei_omf_len5 += 1
    elif len(imei) == 6:
        imei_omf_len6 += 1
    elif len(imei) == 7:
        imei_omf_len7 += 1
    elif len(imei) == 8:
        imei_omf_len8 += 1
    elif len(imei) == 9:
        imei_omf_len9 += 1
    elif len(imei) == 10:
        imei_omf_len10 += 1
    elif len(imei) == 11:
        imei_omf_len11 += 1
    elif len(imei) == 12:
        imei_omf_len12 += 1
    elif len(imei) == 13:
        imei_omf_len13 += 1
    elif len(imei) == 14:
        imei_omf_len14 += 1
    elif len(imei) == 15:
        imei_omf_len15 += 1
    elif len(imei) == 16:
        imei_omf_len16 += 1
    elif len(imei) >= 17:
        imei_omf_len17 += 1
def IMEI_Len_count_ORF(imei):
    global imei_orf_len1;global imei_orf_len2;global imei_orf_len3;global imei_orf_len4;global imei_orf_len5;global imei_orf_len6;global imei_orf_len7;global imei_orf_len8;global imei_orf_len9;global imei_orf_len10;global imei_orf_len11;global imei_orf_len17;global imei_orf_len12;global imei_orf_len13;global imei_orf_len14;global imei_orf_len15;global imei_orf_len16
    if len(imei) == 0:
        pass
    elif len(imei) == 1:
        imei_orf_len1 += 1
    elif len(imei) == 2:
        imei_orf_len2 += 1
    elif len(imei) == 3:
        imei_orf_len3 += 1
    elif len(imei) == 4:
        imei_orf_len4 += 1
    elif len(imei) == 5:
        imei_orf_len5 += 1
    elif len(imei) == 6:
        imei_orf_len6 += 1
    elif len(imei) == 7:
        imei_orf_len7 += 1
    elif len(imei) == 8:
        imei_orf_len8 += 1
    elif len(imei) == 9:
        imei_orf_len9 += 1
    elif len(imei) == 10:
        imei_orf_len10 += 1
    elif len(imei) == 11:
        imei_orf_len11 += 1
    elif len(imei) == 12:
        imei_orf_len12 += 1
    elif len(imei) == 13:
        imei_orf_len13 += 1
    elif len(imei) == 14:
        imei_orf_len14 += 1
    elif len(imei) == 15:
        imei_orf_len15 += 1
    elif len(imei) == 16:
        imei_orf_len16 += 1
    elif len(imei) >= 17:
        imei_orf_len17 += 1



def write_dic():
        keys = kpidic.keys()
        keys.sort()

        with open(testPath+'/Mass-Rat_Loc-Events_combination.csv','w') as newfile1:
                newfile1.write('RAT'+','+'LOCATION METHOD'+','+'EVENT'+','+'COUNT'+'\n')
                for key in keys:
                        value = kpidic[key]
                        keys_1 = key.split('-')
                        keys_2 = ','.join(keys_1)
                        newfile1.write(keys_2+','+str(value)+'\n')
'''
def write_dict():
    cgi_keys = uniq_dict.keys()
    with open(testPath+'/Unique_CGI_GSM.csv','w') as GSM:
        with open(testPath+'/Unique_CGI_UMTS.csv','w') as UMTS:
            with open(testPath+'/Unique_CGI_LTE.csv','w') as LTE:

                GSM.write('CGI'+','+'RAT'+'\n')
                UMTS.write('CGI'+','+'RAT'+'\n')
                LTE.write('CGI'+','+'RAT'+'\n')
                for key2 in cgi_keys:
                    value1 = uniq_dict[key2]
                    cgi_rat_value = key2.split('_')
                    cgi_value= cgi_rat_value[0]
                    if value1 == 'UMTS':
                        UMTS.write(str(cgi_value)+','+str(value1)+'\n')
                    elif value1 == 'LTE':
                        LTE.write(str(cgi_value)+','+str(value1)+'\n')
                    else:
                        GSM.write(str(cgi_value)+','+str(value1)+'\n')
'''
def write_dict():
    cgi_keys = uniq_dict.keys()
    with open(testPath+'/Unique_CGI_RAT.csv','w') as GSM:

        GSM.write('CGI'+'\t'+'\t'+'RAT'+'\n')
        for key2 in cgi_keys:
            value1 = uniq_dict[key2]
            cgi_rat_value = key2.split('_')
            cgi_value= cgi_rat_value[0]
            GSM.write(str(cgi_value)+'\t'+'----->'+str(value1)+'\n')


mass_analysis(mass_output)
write_dic()
write_dict()
elapsed_time_secs = time.time() - start_time
print "Execution completed in",elapsed_time_secs,"seconds"
