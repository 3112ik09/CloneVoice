# Voice Cloning:
### Task : To clone someone's voice and use it in other language . 
**Eg used : Elon Musk 30 sec video to Elon Hindi Musk .....**

### Results:

#### INPUT mP3 - - > >  https://drive.google.com/file/d/1wT0EvH3GJgok24f8AC8IehZjlbDnofwT/view?usp=sharing

#### OUTPUT mP3 - - > > https://drive.google.com/file/d/1lOtI1V6v-VVRmJtnvO9QzATGagbevJzT/view?usp=sharing



<br>

# Steps: 

## 1. Download video and extract audio . eg elon2.wav

## 2. Covert english to hindi (Speech to hindi text)
used open ai free whisper (an automatic speech recognition model trained on 680,000 hours of multilingual data collected from the web.)

Google Translation Api to convert it to Hindi. 

NoteBook: https://drive.google.com/file/d/18fS7tfBgPAGaqWHhuZqHBOSgFRo7uqvb/view?usp=sharing
Kaggle : https://www.kaggle.com/code/ishantkukreti/translate/edit

<hr>

## 3. Convert Clone:
##### Using Bark Ai : 
1. https://github.com/suno-ai/bark
2. https://colab.research.google.com/drive/1RtSbvMfD-yWkNCXdaMTXWiRc71fsmM9f#scrollTo=b5rDDPxrRAKa
3. https://www.youtube.com/watch?v=OHZHM8hcyI4&t=374s

### 1. Approach:
. https://huggingface.co/coqui/XTTS-v1  #do not support hindi
. https://huggingface.co/spaces/BilalSardar/Voice-Cloning
1. dont need a hindi voice model just convert convert Hindi script to Roman script . Use english model to speek. <br><br>
**Hindi : जैसे, जीवन में मेरे द्वारा सामना किए गए सबसे कठिन विकल्पों में से एक 2008 में था।**<br><br>
**Roman : jaise, jIvana meM mere dvArA sAmanA kie gae sabase kaThina vikalpoM meM se eka 2008 meM thA|**

2. Bark ai Hindi Speeker https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c
3. Train a Bark clone model of elon voice. 
4. Then convert Roman script to hindi speech .


Used this Model Links: https://github.com/rsxdalv/tts-generation-webui
Coqui-ai TTS : https://github.com/coqui-ai/TTS


Disadvantage: Do not sound good cracky voice 
<hr>

### 2. Approach
1. Use Bark.Ai to convert it to a hindi bot speaker. 
2. Use RVC model by kalomaze  https://docs.google.com/document/d/13_l1bd1Osgz7qlAZn-zhklCbHpVRk6bYOuAuB78qmsE/edit#heading=h.qjrl2d41vtmt
3. Model Download from : https://docs.google.com/spreadsheets/d/1tAUaQrEHYgRsm1Lvrnj14HFHDwJWl0Bd9x0QePewNco/edit#gid=1227575351 
4. Decent Conversion


