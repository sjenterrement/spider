import re
import numpy as np 
from keras.models import Sequential
from keras.layers import Dense, Activation

paper1 = '''
In President Donald Trump's world view, currency manipulation is bad, except when he's the one calling the shots. Usurping the Treasury Department's 
imminent report on global foreign exchange policy, Trump told the Wall Street Journal the dollar is “getting too strong,” igniting a slump in the 
greenback just as traders in the U.S. were wrapping up.
'''
paper2 = '''
The comments, which saw him also back down on a long-held vow to label China a currency manipulator, were widely viewed as jawboning, putting the U.S. 
in the same basket as the FX-market tinkerers Trump and American officials have so heavily criticized in the past.
'''
paper3 = '''
A group of Tesla Inc(TSLA.O) investors has urged the luxury electric car maker to add two new independent directors to its board, without ties to Chief 
Executive Elon Musk, to "provide a critical check on possible dysfunctional group dynamics." A defiant Musk took to Twitter on Wednesday afternoon to 
suggest the investors buy stock in Ford Motor Co(F.N) instead. The Ford family controls the Detroit automaker through two classes of stock.
'''
paper4 = '''
In a letter dated Monday, five investment groups including the California State Teachers Retirement System, Hermes Equity Ownership Services and CtW 
Investment Group urged Tesla to have all of its directors re - elected annually. "We expect that as companies make the transition to publicly-traded 
status, the governance structures and practices in place at the time of the IPO will evolve to align with the company's changing strategy," the letter 
reads. "However, Tesla's seven-member board is largely unchanged from its pre-IPO days."
'''
paper5 = '''
Led by the enigmatic Musk, Tesla recently became the most valuable U.S. car company, passing General Motors Co(GM.N) for the top spot. Tesla's market 
value has since slipped to just shy of GM's. As of Wednesday, the market cap of the Silicon Valley automaker was $50.3 billion, while GM's was $50.8 
billion. "This investor group should buy Ford stock," Musk posted on Twitter on Wednesday afternoon. "Their governance is amazing..." Musk then said on 
Twitter that he would follow up soon on an earlier promise to appoint more independent directors, "but this (investor) group has nothing to do with it."
'''
paper6 = '''
Over the past month, Tesla stock has surged 35 percent as investors bet that Musk will revolutionize the automobile and energy industries. The shares 
closed down 3.8 percent at $296.84 in Wednesday's trading on Nasdaq, however. Among those on Tesla's board is Kimbal Musk, the CEO's brother, and Brad 
Buss, who served as chief financial officer at SolarCity Corp, which the electric car maker acquired last year.
'''
paper7 = '''
Lawyers for a passenger forcibly removed from a United Airlines flight have filed an emergency court request for the airline to preserve evidence. David 
Dao was filmed being dragged off the overbooked flight at Chicago O'Hare airport, bloodied and screaming, in a video watched millions of times online. United 
Airlines said it would refund the ticket costs of all passengers on Sunday's flight. The airline's chief executive, Oscar Munoz, is insisting he will not resign. 
As of Tuesday, Mr Dao was still recovering in a Chicago hospital, his lawyer said, but a family member is expected to give a news conference on Thursday.
'''
paper8 = '''
China's 2017 export outlook brightened considerably on Thursday as it reported forecast-beating trade growth in March and as U.S. President Donald Trump softened 
his anti-China rhetoric in an abrupt policy shift. Washington's improving ties with Beijing were underscored when Trump told the Wall Street Journal in an interview 
on Wednesday that he would not declare China a currency manipulator as he had pledged to do on his first day in office.
'''
paper9 = '''
The comments were an about-face from Trump's campaign promises, which had rattled China and other Asian exporters, and came days after his first meeting with President 
Xi Jinping where he pressed China to help rein in North Korea. China's exports rose at the fastest pace in a little more than two years in March, climbing 16.4 percent 
from a year earlier in a further sign that global demand is improving, the customs office reported on Thursday.
'''
paper10 = '''
"There are increased signs of warming up in the global economy", which helped China's steady growth in the first quarter, Yan Pengcheng, a spokesman for the country's top 
economic planning agency, told a news conference. Import growth remained strong at 20.3 percent, driven by the country's voracious appetite for oil, copper, iron ore, coal 
and soybeans, whose volumes all surged from February despite worries about rising inventories.
'''
paper11 = '''
China's crude oil imports hit a record high of nearly 9.2 million barrels per day, overtaking the United States. The stronger trade data reinforced the growing view that 
economic activity in China has remained resilient or is even picking up, adding oomph to a global manufacturing revival, though analysts say growth in imports could slow.
'''
paper12 = '''
"Right now domestic demand is still quite stable and robust. But the ultimate driver actually is property investment (which) we expect to slow," Nomura economist Yang Zhao 
said. Zhao expects import growth will moderate to the high-single digits in the second quarter. Imports had surged 38 percent in February while exports unexpectedly dipped, 
but China's data in the first two months of the year can be heavily skewed by the timing of the Lunar New Year holidays, when many businesses shut for a week or more.
'''
paper13 = '''
Analysts polled by Reuters had expected March exports to have increased by 3.2 percent from a year earlier, a rebound from a 1.3 percent drop in February. Imports had been 
forecast to rise 18.0 percent, after surging 38.1 percent in February. China reported a trade surplus of $23.93 billion for March. Analysts had expected the trade balance to 
return to a surplus of $10.0 billion in March, after it reported its first trade gap in three years in February.
'''
paper14 = '''
The Trump administration has proposed whacking the budget of the Environmental Protection Agency by nearly a third, eliminating thousands of employees and scrapping dozens of 
programs, including climate-change research and cleanup efforts in the Great Lakes and Chesapeake Bay. But a detailed budget plan obtained by The Washington Post last week includes 
a request to add positions within the agency’s Office of Enforcement and Compliance Assurance  “to provide 24/7 security detail” for EPA Administrator Scott Pruitt. Pruitt’s 
predecessor, Gina McCarthy, had what was known as “door-to-door” protection — essentially from her residence each morning until she returned at night, according to Liz Purchia, a 
communications director at the EPA in the Obama administration.
'''
paper15 = '''
She said security officers typically would leave McCarthy once she was at her office. Previous EPA administrators have had similar arrangements. On a handful of international 
trips, McCarthy did receive 24/7 protection, depending on the threat level of a country, as determined by the State Department, Purchia said. But that was the exception rather 
than the rule. And if McCarthy was in Washington over the weekend, her security detail would not be with her unless she had an official event.
'''
paper16 = '''
New Delhi, Jan 9 () Russia U-18 hammered India's U-17 World Cup squad 8-0 in a Group B match of the Valentin Granatkin Memorial Cup in St. Petersburg. The result could have been 
worse had not Russia missed a penalty just before the half time. The hosts led lead 5-0 at the interval late last night. The first goal came as early as the 2nd minute when Glushkov 
headed in the first corner of the match. It wasn't the start which the Indians were looking for. The second goal came off another corner in the 12th minute this time Goalkeeper 
Dheeraj Singh fumbling to collect it and it was gleefully tapped in by Denisov.
'''
paper17 = '''
Glushenkov made it 3-0 in the 21t minute. He followed up a long ball played behind the defence, beat his marker for speed and lobbed it over Dheeraj. Rudenko made it 4-0 in the 
25th minute and Gluskenov scored his second in the 31st to make it 5-0. Following a cross from the left, he trapped in between the two defenders and made space with a deft feint 
to blast it in. Russia scored the sixth goal immediately after the changeover when Tsypchenko tapped it in after dribbling past Boris Singh. It was 7-0 in the 67th minute -- this 
time Tsypchenko heading in a corner.
'''
paper18 = '''
With nine substitutions being allowed in the match, coach Nicolai Adam brought in as many as six substitutions but they failed to make any impact. Late in the second half, India did 
have a shy at the rival goal but first, Sanjeev's shot sailed wide and then Komal's shot went straight to the rival goalkeeper. Latchevic completed the rout in added time when he made 
no mistake to slot in from the penalty spot. India next play Belarus U-18 team tomorrow. AH AH Stay updated on the go with Times of India News App. Click here to download it for your 
device.
'''
paper19 = '''
Jose Mourinho insists Manchester United will field a strong side for Sunday's clash with former club Chelsea at Old Trafford, live on Sky Sports. United face Anderlecht in Belgium 
on Thursday before they host the league leaders this weekend followed by the second leg of the Europa League quarter-final at Old Trafford next week.
'''
paper20 = '''
Didier Drogba says Chelsea fans should not rule out seeing Romelu Lukaku back at Stamford Bridge next season. And the former Chelsea striker says he knows what Lukaku - who he 
calls his "little brother" from their time together in west London - will do this summer. The Everton striker, who has scored 24 Premier League goals this season, has been heavily 
linked with a move away from Goodison Park and recently said he would not sign a new deal - although his agent, Mino Raiola had previously said a deal was '99.9 per cent' done.
'''

papers = [paper1, paper2, paper3, paper4, paper5, paper6, paper7, paper8, paper9, paper10, paper11, paper12, 
		  paper13, paper14, paper15, paper16, paper17, paper18, paper19, paper20]
labels = np.array([[1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], 
	[0, 1], [0, 1], [0, 1], [0, 1], [0, 1]])

sp = re.compile('\W')
voca = []
for paper in papers:
	filteredwords = [_.lower() for _ in sp.split(paper) if _]
	voca.extend(filteredwords)
voca = list(set(voca))  #去重

x_data = []
for paper in papers:
	vword = np.zeros(761)
	filteredwords = [_.lower() for _ in sp.split(paper) if _]
	for word in filteredwords:
		vword[voca.index(word)] += 1
	x_data.append(vword)

x_data = np.array(x_data)

model = Sequential()
model.add(Dense(761, input_dim=761))
model.add(Activation('sigmoid'))
model.add(Dense(2))
model.add(Activation('softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
model.fit(x_data[2:, :], labels[2:, :], batch_size=18, epochs=10, verbose=True)
model.evaluate(x_data[:2, :], labels[:2, :], batch_size=2, verbose=1)
#print(model.predict(x_data[:2, :]))
pre_result = model.predict(x_data[:2, :])
if(pre_result[0][0] > pre_result[0][1]):
	print('该文章为财经类文章')
else:
	print('该文章为体育类文章')
if(pre_result[1][0] > pre_result[1][1]):
	print('该文章为财经类文章')
else:
	print('该文章为体育类文章')
input()