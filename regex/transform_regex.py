# Adds variables in to regex to create complex regex

import os
import json


month_name = "(J|j)an(uary)?|JAN(UARY)?|(F|f)eb(ruary)?|FEB(RUARY)?|(M|m)ar(ch)?|MAR(CH)?|(A|a)pr(il)?|APR(IL)?|May|MAY|(J|j)un(e)?|JUN(E)?|(J|j)ul(y)?|JUL(Y)?|(A|a)ug(ust)?|AUG(UST)?|(S|s)ep(tember)?|SEP(TEMBER)?|SEPT|Sept|(O|o)ct(ober)?|OCT(OBER)?|(N|n)ov(ember)?|NOV(EMBER)?|(D|d)ec(ember)?|DEC(EMBER)?"

hos_kor = "단국대학교의과대학부속|이화여자대학교의과대학|서울대학교 강남센터|연세대학교세브란스|가톨릭대학교성모|대구가톨릭대학교|계명대학교동산|분당서울대학교|양산부산대학교|칠곡경북대학교|AJOUMC|강남세브란스|대구가톨릭대|순천향대학교|신촌세브란스|CAUMC|CBNUH|HYUMC|KBSMS|KNUCH|PNUYH|SCHMC|SNUBH|SNUCH|건국대학교|경북대학교|경상대학교|경희대학교|고려대학교|동아대학교|단국대학교|부산대학교|분당서울대|서울대학교|아주대학교|양산부산대|영남대학교|울산대학교|원광대학교|이화여자대|전남대학교|전북대학교|중앙대학교|충남대학교|충북대학교|칠곡경북대|한양대학교|AJOU|CNUH|DAMC|DCMC|DKUH|DSMC|EUMC|GNUH|JBUH|KHUH|KNUH|KUMC|PNUH|SNUH|WKUH|YUMC|가톨릭대|강남센터|강북삼성|구가톨릭|분당서울|삼성서울|서울아산|순천향대|양산부산|이화여대|이화여자|칠곡경북|AMC|CMC|DMC|KUH|SMC|UUH|가톨릭|건국대|경북대|경상대|경희대|계명대|고려대|단국대|동아대|보라매|부산대|분당차|서울대|순천향|아주대|연세대|영남대|울산대|원광대|전남대|전북대|중앙대|충남대|충북대|한양대|건국|건대|경북|경상|경희|계명|고대|고대|고려|단국|동아|본원|부산|삼성|서울|성모|신촌|아산|아주|안암|연건|연대|연세|영남|울산|원광|전남|전북|중앙|충남|충대|충북|한양"

# Get blacklisted names
# names_blacklist = json.loads(open("../../filters/blacklists/names_blacklist_ssfirst.json").read())
# person_names = ''
# for key in names_blacklist:
# 	person_names += key + '|'
# # Get rid of last pipe
# person_names = person_names[:-1]

# Do folder walk and transform each file
rootdir = '.'
for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		if ".txt" in file and "_transformed.txt" not in file and "catchall" not in file:
			filepath = os.path.join(subdir, file)
			# Get currnet file name and create transformed name
			file_root = file.split(".")[0]
			new_file_name = file_root + "_transformed.txt"
			new_filepath = os.path.join(subdir, new_file_name)
			# Open file
			regex = open(filepath,"r").read().strip()
			# Replace variables
			regex = '\S*' + regex + '\S*'
			regex = regex.replace('"""+month_name+r"""', month_name).replace('"""+hos_kor+r"""', hos_kor)
			# Write new file
			with open(new_filepath, "w") as fin:
				fin.write(regex)







