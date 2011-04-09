# -*- coding: utf-8 -*-
from django.core.management import setup_environ

import forms.form_models.bfsql as bfsql
import forms.form_models.bform as bforms
from forms.form_models.bfbdb import *

bf = bforms.BerkeleyForm()
bf.theme='nain'
bf.doctype='html'
bf.name='nain'

qdb = [
	{'type':'Section','label':'I.	Your Organization','style':'section'},
		
		{'type':'Section','label':'A) Check the phrase that best describes your organization','style':'subsection'},
		{'type':'CheckOne',
			'choices':('local interfaith group','regional, national or international interfaith group',
			'division of a regional, national or international body representative of a faith community in Canada, the United States or Mexico',
			'academic institution, study center or other organization concerned with religious education on a Multifaith basis',
			'media body concerned with different religious traditions and/or relationships among them.')
		},
		{'type':'CloseTag'},
		{'type':'Section','label':'B) Members of your organization are made up of:',
			'style':'subsection'},		
			{'cons': (('max', '5'),),  'type':'Text','label':'Number of Members ','cons':(('required',False),)},
			{'type':'Text','label':'Number of Congregations ','cons':(('required',False),)},
			{'type':'Text','label':'Number of Religions Represented ','cons':(('required',False),)},
			{'type':'Text','label':'Number of Organizations ','cons':(('required',False),)},
			{'type':'Text','label':'Number of Agencies ','cons':(('required',False),)},
			{'type':'Text','label':'Number of Institutions','cons':(('required',False),)},
		{'type':'CloseTag'},
		{'type':'Section','label':'C) Briefly share the Mission or Purpose Statement of your organization.',
			'style':'subsection'},
			{'type':'TextArea','cons':(('required',False),)},
		{'type':'CloseTag'},
		{'type':'Section','label':'D) How is your mission or purpose achieved? Check all that apply.', 'style':'subsection'},
			{'type':'CheckMany','label':'Programs involve:','cons':(('required',False),),
				'choices':('interfaith dialogue','advocacy','academic study') },
			{'type':'CheckMany','label':'Dialogue includes','cons':(('required',False),),
				'choices':('workshops','seminars','retreats','conferences')},
			{'type':'CheckMany','label':'Advocacy includes','cons':(('required',False),),
				'choices':('service projects','visits to religious centers','lobbying')},
			{'type':'CheckMany','label':'Activities are in cooperation with other','cons':(('required',False),),
				'choices':('local','regional','national','international groups')},
			{'type':'CheckMany','label':'The organization has its own sub-groups in','cons':(('required',False),),
				'choices':('local','regional','national','international areas')},
		{'type':'CloseTag'},
		{'type':'Section','label':'E) How often does your organization meet?','style':'subsection'},
			{'type':'CheckOne','choices':('Weekly','Monthly','Quarterly','Semi-annually','Annually','Other'),'cons':(('required',False),)},
			{'type':'CheckOne','label':'Has your organization','choices':('grown or','declined in membership in the past five years?'),'cons':(('required',False),)},
			{'type':'CheckOne','label':'Has your organization','choices':('grown or ','declined in programming activity in the past five years?'),'cons':(('required',False),)},
			{'type':'CheckOne','label':'Has your organization','choices':('grown or ','declined in community service in the past five years?'),'cons':(('required',False),)},
		{'type':'CloseTag'},
		{'type':'Section','label':'F) Briefly describe one of your organizations\' most successful interfaith programs.','style':'subsection'},
			{'type':'TextArea','cons':(('required',False),)},
		{'type':'CloseTag'},
		{'type':'Section','label':'G) This success is based upon: check all that apply','style':'subsection'},
			{'type':'CheckMany','cons':(('required',False),),
			'choices':
				('number of participants','quality of interfaith dialogue','development of further interfaith activity',
				'education of participants', 'quality of interfaith advocacy', 'quality of service offered',
				'number of people reached','amount of money raised for the organization')
			},
	{'type':'CloseTag'},
	{'type':'Section','label':'II.	NAIN and Your Organization','style':'section'},
	
		{'type':'Section','label':'A)	How Interfaith Organizations Participate in NAIN ','style':'subsection'},
			{'type':'CheckOne','label':'2. Our organization has participated in NAINConnects',
				'choices':('Yes','No')},
			{'type':'CheckOne','label':'2.	I have personally participated','choices':('Yes','No')},
			{'type':'CheckMany','label':'Check all of the NAINConnects in which your organization has participated:','cons':(('required',False),), 
				'choices':('1988 Wichita','1990 Seattle','1992 Berkeley','1994 Toronto','1996 Dallas','1997 Columbia',
				'1998 Edmonton','1999 Chautauqua','2000 Fullerton','2001 Beausejour','2002 Wichita','2003 Columbus','2004 New York City',
				'2005 Las Vegas','2006 Vancouver','2007 Richmond','2008 San Francisco')},
			{'type':'CheckOne','label':'3.	Will your organization participate in the 2009 NAINConnect in Kansas City? ',
				'choices':('Yes','No')},
			{'type':'CheckOne','label':'4.	Will you personally attend the 2009 NAINConnect?',
				'choices':('Yes','No','Maybe')},
			{'type':'CheckOne','label':'5.	Has a member of your organization ever served as a Board member of NAIN',
				'choices':('Yes','No')},
			{'type':'Text','label':'Name of Member','cons':(('required',False),)},
			{'type':'Text','label':'Years Served','cons':(('required',False),)},
			{'type':'CheckOne','label':'6.	Has your organization ever provided a committee member to NAIN?',
				'choices':('Yes','No')}, #possible use of unsupported sub-items
				{'type':'Text','label':'Name of Member', 'cons':( ('required',False) ,) },
				{'type':'Text','label':'Committee','cons':( ('required', False) ,) },
			{'type':'CheckOne','label':'7.	Has your organization encouraged other interfaith groups to join NAIN? ',
				'choices':('Yes','No')},
			{'type':'CheckOne','label':'8.	Is your organization ready to participate more directly in NAIN?',
				'choices':('Yes','No','with a Board member','with a Committee member','in NAIN membership recruitment',
				'with articles for NAINews ','don\'t know','already doing so')},
		{'type':'CloseTag'},
		{'type':'Section','label':'B)	How interfaith organizations can network through NAIN: ','style':'subsection'},
			{'type':'CheckOne','label':'1. NAINConnects have helped our organization network: ',
				'choices':('Yes','No')},
			{'type':'CheckOne','label':'NAINConnects have helped me to network:',
				'choices':('Yes','No')},
			{'type':'CheckMany','label':'3. Check ways in which your organization has networked at NAINConnects:','cons':(('required',False),),
				'choices':('strengthened interaction with other interfaith professionals',
					'strengthened interaction with other interfaith organizations',
					'found speakers or spiritual leaders to help our organization; brought them to our group ',
					'learned of new programs for interfaith dialogue; adapted them to our organization',
					'learned of new interfaith advocacy activities: adapted them to our organization ',
					'learned new methods for networking within the national/international interfaith community',
					'strengthened diversity training and interfaith skills through Open Space process used at some Connects',
					'gained knowledge about individual world religions and their presence in the local community',
					'\'national community')},
			{'type':'TextArea','label':'4.	Suggested improvements for NAINConnects',
				'cons':(('required',False),)},
			{'type':'CheckMany','label':'5.	NAINews has been helpful to our organization:','cons':(('required',False),),
				'choices':('through articles on interfaith initiatives around the continent at the local level',
				'national level',
				'international level',
				'through announcements re: upcoming interfaith initiatives around the continent',
				'through its articles on issues that impact the interfaith movement',
				'through its in-depth exploration of issues pertinent to our times',
				'through its interview / information on interfaith and spiritual leaders',
				'through its articles concerning world religions',
				'We have contributed articles or published information about our organization\'s work in NAINews.',
				'has not been useful',
				)},
			{'type':'CheckMany','label':'6.	NAINOnline has been helpful to our organization:','cons':(('required',False),),
				'choices':('through its library of interfaith materials and resources',
					'through its publication of NAINews',
					'through its directory of member organizations',
					'through its young adult section',
					'through its interfaith links',
					'through its links to websites of world religions and related groups',
					'has not been useful',
			),}, #other field required - add this.
			{'type':'Text','label':'other','cons':( ('required',False),)},
			
		{'type':'CloseTag'},
	{'type':'CloseTag'},
	{'type':'Section','label':'III.	New Directions for NAIN','style':'section'},
	
		{'type':'Section','label':'A)	Beneficial new initiatives for NAIN might include (check those of interest to your organization):','style':'subsection'},
			{'type':'CheckMany','cons':(('required',False),),'choices': (
				'occasional regional meetings as well as the annual NAINConnect',
				'support visits by NAIN Board to member organizations to learn of their successes and needs.',
				'monthly reports on these visits to all NAIN members',
				'publication of a directory of North American interfaith organizations that is kept current',
				'monthly conference calls in which leaders share their expertise on particular aspects of interfaith work',
			)},
		{'type':'CloseTag'},
		{'type':'Section','label':'B)	New directions for NAIN might include','style':'subsection'},
			{'type':'CheckMany','cons':(('required',False),),'choices':(
				'NAIN pilgrimages to sacred sites in North America',
				'NAIN pilgrimages to sacred sites outside of North America',
				'NAIN guidelines for interfaith and multicultural living in wake of 9/11',
				'Connecting NAIN with interfaith / religious organizations on the other continents',
				'NAIN Success Stories: anthology of member organizations’ interfaith program success stories',
				'Seeking grants and other funding to expand the scope of our work',
			)},
		{'type':'CloseTag'},
		{'type':'Section','label':'C)	Our organization could benefit from the visit of a NAIN Board member by','style':'subsection'},
			{'type':'CheckMany','cons':(('required',False),),
			'choices':(
				'assistance with beginning an interfaith group in our community',
				'assistance with developing interfaith guidelines',
				'assistance in developing advocacy  and/or',
				'dialogue programs in our area',
				'seeing and promoting our successful interfaith programs to other communities'
			)},
		{'type':'CloseTag'},
		{'type':'Section','label':'D)	Do you know of any funding sources (foundations, individuals, congregations) that NAIN should be exploring?','style':'subsection'},
			{'type':'Text','label':'Name of Source ','cons':(('required',False),)},
			{'type':'Text','label':'Contact Person ','cons':(('required',False),)},
			{'type':'Text','label':'Address','cons':(('required',False),)},
			{'type':'Text','label':'City','cons':(('required',False),)},
			{'type':'Text','label':'State / Provence','cons':(('required',False),)},
			{'type':'Text','label':'Code','cons':(('required',False),)},
			{'type':'Text','label':'Phone','cons':(('required',False),)},
			{'type':'Text','label':'Fax','cons':(('required',False),)},
			{'type':'Text','label':'E-Mail','cons':(('required',False),)},
			{'type':'Text','label':'Website ','cons':(('required',False),)},
		{'type':'CloseTag'},
		{'type':'Section','label':'E) Additional Comments You Wish to Share ','style':'subsection'},
			{'type':'TextArea','cons':(('required',False),)},
		{'type':'CloseTag'},
	{'type':'CloseTag'},
	]

bforms.createQuestions(bf,qdb)
saveObject(bf)