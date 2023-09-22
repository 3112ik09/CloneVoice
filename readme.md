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

* Kaggle : https://www.kaggle.com/code/ishantkukreti/translate/edit

<hr>

## 3. Convert Clone:
##### Using Bark Ai : 
1. https://github.com/suno-ai/bark

### 1. Approach:  (BarkAi + Coqui-Ai)
Result: https://drive.google.com/file/d/1rXM2DGEHaJwZ1Jz1K-2zHHTRsgiBTjEt/view?usp=sharing
* https://huggingface.co/coqui/XTTS-v1  #do not support hindi
1. dont need a hindi voice model just convert convert Hindi script to Roman script . Use english model to speek. <br><br>
**Hindi : जैसे, जीवन में मेरे द्वारा सामना किए गए सबसे कठिन विकल्पों में से एक 2008 में था।**<br><br>
**Roman : jaise, jIvana meM mere dvArA sAmanA kie gae sabase kaThina vikalpoM meM se eka 2008 meM thA|**

2. Bark ai Hindi Speaker 
3. Train a Bark clone model of elon voice. 
4. Then convert Roman script to hindi speech .


Used this Model Links: https://github.com/rsxdalv/tts-generation-webui
Coqui-ai TTS : https://github.com/coqui-ai/TTS


Disadvantage: Do not sound good cracky voice 
<hr>

### 2. Approach
1. Use Bark.Ai to convert it to a hindi bot speaker.   https://drive.google.com/file/d/1hyua_x3-FbzdYikx8ylOfxI8NLPe6w1C/view?usp=sharing
2. Use RVC model by kalomaze  https://docs.google.com/document/d/13_l1bd1Osgz7qlAZn-zhklCbHpVRk6bYOuAuB78qmsE/edit#heading=h.qjrl2d41vtmt
3. Decent Conversion


