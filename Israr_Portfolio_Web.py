import streamlit as st
from pathlib import Path
from streamlit_option_menu import option_menu
import streamlit.components.v1 as com
import google.generativeai as genai
from PIL import Image
import requests
from streamlit_lottie import st_lottie

api_key =st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
st.set_page_config(
    page_title="Israr Ahmad Portfolio",
    page_icon=":wave:",
)

st.markdown(
    """
    <style>
    
    .fade-in {
        opacity: 0;
        animation: fadeInAnimation ease 2s;
        animation-iteration-count: 1;
        animation-fill-mode: forwards;
    }
    @keyframes fadeInAnimation {
        0% {opacity: 0;}
        100% {opacity: 1;}
    }
    .bordered-image {
        border: 10px solid #000;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50; 
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .stButton>button:hover {background-color: #45a049;}
    img {
        border: 0px solid #fff;
        border-radius: 10px;
        animation: fadeInAnimation ease 2s;
        animation-iteration-count: 1;
        animation-fill-mode: forwards;
    }
    img:hover {transform: scale(1.05);}
    </style>
    """,
    unsafe_allow_html=True
)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/style.css")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

resume_file = current_dir / "assets" / "ISRAR AHMAD CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic1.png"

# ---side bar menu----
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Achievements", "Skills", "Comp Vision Projects", "Arduino Projects", "Deep Learning Projects",
                 "Comp Vision Games", "Teaching Experience", "Israr's AI Bot", "Contact"],
        icons=['house-add-fill', 'award-fill', 'mask', 'cast', 'cpu', 'laptop-fill', 'bullseye', 'book-half', 'robot',
               'envelope'],
    )

    # ----Home page----
if selected == "Home":

    NAME = "Israr Ahmad"
    DESCRIPTION = """
    Computer Vision App Developer | Computer Vision Game Developer | Deep Learning | Arduino Projects Developer | Web Developer | Educator  
    """
    EMAIL = "azlanshly@email.com"
    SOCIAL_MEDIA = {
        "YouTube": "https://youtube.com",
        "LinkedIn": "https://linkedin.com",
        "GitHub": "https://github.com",
        "Twitter": "https://twitter.com",
    }

    # --- LOAD CSS, PDF & PROFIL PIC ---
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)

    # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

    # --- SOCIAL media LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

    # --- QUALIFICATIONS & ACHIEMENTS ---
    st.write('\n')
    st.subheader("Qulaification & Achievements")
    st.write(
        """
    - ✔️ Completed M.Phil in Computer Science.
    - ✔️ Successfully developed various computer vision projects.
    - ✔️ Desgined and built innovative Arduino projects.
    - ✔️ Demonstrated experties in image processing,object detection, face recognition.

    """
    )
    st.write('---')

    # --- SKILLS ---
    com.html("""
        <div>
            <style>
            h1.heading {
                background-color: #d33682;
                color: white;
                margin-bottom:300;
                border-radius: 10px;
                text-align: center;
            }
            </style>
            <h1 class="heading">Skills</h1>
            <p></p>
        </div>
        """, height=60, )
    st.write(
        """
    - 👩‍💻 Python
    - 📊 Java
    - 📚 PHP
    - 👩‍💻 C/C++
    - 📊 Html
    - 📚 CSS
    - 🗄️ Databases: (MySQL, SQL Server)
    - 👩‍💻 Computer Vision (Hand tracking,Object detection,Face recognition,image processing
    - 📚 Hardware (Arduino,sensors,cameras)
    - 🚧 Frameworks/Libraries
    - 👩‍💻 Tensorflow
    - 📊 Opencv
    - 📚 cvzone
    - 🗄️ Hugging Face
    - 👩‍💻 Arduino Libraries


    """
    )

    # ---COMPUTER VISION PROJECTS
    st.write('---')
    com.html("""
    <div>
        <style>
        h1.heading {
            background-color: #d33682;
            color: white;
            border-radius: 10px;
            text-align: center;
        }
        </style>
        <h1 class="heading">Computer Vision Projects</h1>
        <p></p>
    </div>
    """, height=60)

    st.write(
        """
    - ☀️ Helmet detection system using Custom Trained YOLO model
    - ☀️ Bag counter using Custom trained YOLO model
    - ☀️ Vehicle counting system using YOLO V8
    - ☀️ Person counting system using YOLO V8
    - ☀️ Bottle counting system on conveyor belt using YOLO V8
    - ☀️ Detecting and counting faces in images using YOLO V8
    - ☀️ Situp counter Posedetector from cvzone
    - ☀️ Pushup Counter using Posedetector from cvzone
    - ☀️ Hand gesture controlled lights using handtracking module from cvzone
    - ☀️ Hand detection and finger counter system
    - ☀️ Intelligent surveilliance camera 
    - ☀️ Face Recognition system 
    - ☀️ License plate detection system



    """
    )

    com.html("""
                         <div>
                             <style>
                             h1.heading {
                                 background-color: #d33682;
                                 color: white;
                                 border-radius: 10px;
                                 text-align: center;
                             }
                             </style>
                             <h1 class="heading">Computer Vision projects Gallery</h1>
                             <p></p>
                         </div>
                         """, height=60)
    st.write('\n')

    col1, col2 = st.columns(2)

    with col1:

        st.image("images/1.jpg", use_column_width=True, caption="Counting People in an image")
        st.image("images/2.jpg", use_column_width=True,caption="Push Up Counter")
        st.image("images/3.jpg", use_column_width=True,caption="Face Recognition System")

    with col2:
        st.image("images/4.jpg", use_column_width=True,caption="Bottle Counting System")
        st.image("images/5.jpg", use_column_width=True,caption="Vehicle classification and counting System")
        st.image("images/6.jpg", use_column_width=True,caption="Car Parking Space Counting System")

    st.write('---')

    # ---ARDUINO PROJECTS
    st.write('---')
    com.html("""
      <div>
          <style>
          h1.heading {
              background-color: #d33682;
              color: white;
              border-radius: 10px;
              text-align: center;
          }
          </style>
          <h1 class="heading">Arduino Projects</h1>
          <p></p>
      </div>
      """, height=60)

    st.write(
        """
    - ☀️ Voice controlled Robot
    - ☀️ Obstacle avoiding Robot using servo motor
    - ☀️ Line follower Robot
    - ☀️ Edge avoiding Robot
    - ☀️ Mobile app controlled Robot car using bluetooth module
    - ☀️ Surveiliance Camera car using ESP32 CAM
    - ☀️ Home light control using mobile app
    - ☀️ Automatic dustbin using ultrasonic sensor
    - ☀️ Smart stick for blind person
    - ☀️ Automatic water dispenswer
    - ☀️ Automatic room light system using PIR sensor
    - ☀️ Fire Alarm System





    """
    )

    com.html("""
                         <div>
                             <style>
                             h1.heading {
                                 background-color: #d33682;
                                 color: white;
                                 border-radius: 10px;
                                 text-align: center;
                             }
                             </style>
                             <h1 class="heading">Arduino projects Gallery</h1>
                             <p></p>
                         </div>
                         """, height=60)
    st.write('\n')
    col1, col2 = st.columns(2)

    with col1:

        st.image("images/7.jpg", use_column_width=True,caption="Voice Controlled Robot")
        st.image("images/8.jpg", use_column_width=True,caption="Obstacle Avoiding Robot Using Servo Motor")
        st.image("images/9.jpg", use_column_width=True,caption="Automatic Room Light")

    with col2:
        st.image("images/10.jpg", use_column_width=True,caption="Line Following Robot")
        st.image("images/11.jpg", use_column_width=True,caption="Android App Controlled Robot")
        st.image("images/12.jpg", use_column_width=True,caption="Smart Dustbin")
    st.write('---')

    # ---Machine Learning/Deep Learning/Streamlit Projects

    st.write('---')
    com.html("""
          <div>
              <style>
              h1.heading {
                  background-color: #d33682;
                  color: white;
                  border-radius: 10px;
                  text-align: center;
              }
              </style>
              <h1 class="heading">Machine Learning/Deep Learning/Streamlit Projects</h1>
              <p></p>
          </div>
          """, height=60)

    st.write(
        """
    - ☀️ Digits classification using tensorflow and keras
    - ☀️ Cats and Dog classification using CNN
    - ☀️ Sentiment analysis
    - ☀️ Portfolio website (streamlit)

    """
    )
    # ---COMPUTER VISION GAMES

    st.write('---')
    com.html("""
          <div>
              <style>
              h1.heading {
                  background-color: #d33682;
                  color: white;
                  border-radius: 10px;
                  text-align: center;
              }
              </style>
              <h1 class="heading">Games using Computer Vision</h1>
              <p></p>
          </div>
          """, height=60)

    st.write(
        """
    - ☀️ Balloon pop game using pygame hand tracking modle
    - ☀️ Snake game using pygame hand tracking module
    - ☀️ Eatable non eatable game using pygame
    - ☀️ Virtual Quiz game using pygame Hand Tracking Module
    - ☀️ Created executable (.exe) files for computer vision games
    - ☀️ Developed installers for computer vision games

    """
    )

    # --- TEACHING EXPERIENCE
    st.write('---')
    com.html("""
             <div>
                 <style>
                 h1.heading {
                     background-color: #d33682;
                     color: white;
                     border-radius: 10px;
                     text-align: center;
                 }
                 </style>
                 <h1 class="heading">Teaching Experience</h1>
                 <p></p>
             </div>
             """, height=60)

    st.write(
        """
    - ☀️ Taught intermediate students (ICS 2nd Year) various projects
    - ☀️ Computer Vision Projects (e.g., hand tracking, object detection)
    - ☀️ Arduino projects (e.g., robotics,automation)
    - ☀️ Developed and delivered curriculum materials, including tutorials and code exam.
    - ☀️ Mentored students in project development, debugging,and problem-solving


    """
    )

    st.write('---')
    com.html("""
                 <div>
                     <style>
                     h1.heading {
                         background-color: #d33682;
                         color: white;
                         border-radius: 10px;
                         text-align: center;
                     }
                     </style>
                     <h1 class="heading">Projects by my students (video links)</h1>
                     <p></p>
                 </div>
                 """, height=60)

    col1, col2 = st.columns(2)
    with col1:
        st.write("☀️☀️☀️Computer Vision Projects☀️☀️☀️")
        st.video("https://youtu.be/Gt4R4AsbeQg?feature=shared")

    with col2:
        st.write("☀️☀️☀️☀️☀️Arduino Projects☀️☀️☀️☀️")
        st.video("https://youtu.be/172nHbDjWnM?feature=shared")

    # --- MY AI BOT

    st.write('---')
    com.html("""
                 <div>
                     <style>
                     h1.heading {
                         background-color: #d33682;
                         color: white;
                         border-radius: 10px;
                         text-align: center;
                     }
                     </style>
                     <h1 class="heading">Israr's AI Bot</h1>
                     <p></p>
                 </div>
                 """, height=60)
    st.write('\n')
    left_column, center_column, right_column = st.columns(3)
    with center_column:
        st.image("images/robo2.gif", use_column_width=True, caption="")

    user_question = st.text_input("Ask anything about me")
    st.write('\n')
    if st.button("ASK", use_container_width=True):
        persona = """
                    You are Israr Ahmad AI bot. You help people answer questions about yourself (i.e. ISRAR).
                    Answer as if you are responding. Don't answer in second or third person.
                    If you don't know the answer, you simply say "That's a secret".
                    Here is more info about Israr Ahmad:
                    ISRAR AHMAD is an educator, computer vision application developer, Arduino project developer, and web developer with a keen interest in learning new technologies.I have created various Arduino robot cars, including line-following, obstacle-avoiding, edge-avoiding, and voice-controlled robot cars. Additionally, I have developed several computer vision projects using OpenCV, such as a bottle counting system, vehicle counting system, bags counting system on a conveyor belt using custom-trained models, person counting system using YOLO model, license plate detection system, hand-controlled light, helmet detection system using custom-trained models, intelligent surveillance camera, and eye blink counter system.I have also created a digits classification system using TensorFlow and Keras, a dogs and cats image classification system using CNN, and a portfolio website using Streamlit.I charge for projects depending on the type, nature, and complexity of the project, as well as the number of live sessions required for debugging. I live in Layyah district, Punjab province, Pakistan.Israr Ahmad obtained his M.Phil degree in Computer Science and has extensive experience in the fields of Arduino and computer vision, later specializing in robotics.I have also worked as a software developer.

He also has skills in programming languages such as Python, PHP, Java, WordPress, Streamlit, HTML, CSS, and databases like MySQL and SQL Server. He has developed interesting educational games using computer vision and Pygame. He has more than 12 years of teaching experience and 5 years of experience in developing Arduino projects.He does not have a YouTube channel but can be contacted via email at azlanshly@gmail.com.He explores different sources to learn technology, such as ChatGPT, Stack Overflow, Google AI Bard, YouTube, various blogs, and websites. He learned Arduino by doing experiments and from the website arduino.cc.
He also has two years of experience in web development. He has developed various websites, such as an online voting system, an online complaint management system, an online mobile shop, and an online watch sales platform. Additionally, he created a comment analyzer using Streamlit and Hugging Face, and worked on sentiment analysis. He also developed a face recognition system using computer vision.
For Arduino projects, he used Arduino Uno, Arduino SMD, and Arduino Nano.
I do not charge for projects for students.
I am lucky to have had so many teachers who changed my life. They are all the best, but in the field of computer vision, Sir Murtaza Hassan is my favorite teacher.




                    Israr's Email: azlanshly@gmail.com 

                    """
        prompt = persona + "Here is the question that the user asked: " + user_question
        response = model.generate_content(prompt)
        st.write(response.text)
        st.write("\n")
    st.write('##')
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write('---')
    com.html("""
                 <div>
                     <style>
                     h1.heading {
                         background-color: #d33682;
                         color: white;
                         border-radius: 10px;
                         text-align: center;
                     }
                     </style>
                     <h1 class="heading">Reach out to me at!</h1>
                     <p></p>
                 </div>
                 """, height=60)
    # st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
           <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
               <input type="hidden" name="_captcha" value="false">
               <input type="text" name="name" placeholder="Your name" required>
               <input type="email" name="email" placeholder="Your email" required>
               <textarea name="message" placeholder="Your message here" required></textarea>
               <button type="submit">Send</button>
           </form>
           """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()


        # lottie_coding = load_lottiefile("lottiefile.json")  # replace link to local lottie file
        # lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")
        lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_lt8ter7g.json")

        st_lottie(
            lottie_hello,
            speed=1,
            reverse=True,
            loop=True,
            quality="low",  # medium ; high
            renderer="svg",  # canvas
            height=None,
            width=None,
            key=None,
        )

if selected == "Achievements":
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    st.subheader("Qulaification & Achievements")
    st.write(
        """
    - ✔️ Completed M.Phil in Computer Science.
    - ✔️ Successfully developed various computer vision projects.
    - ✔️ Desgined and built innovative Arduino projects.
    - ✔️ Demonstrated experties in image processing,object detection, face recognition.

    """
    )
    st.write('---')

if selected == "Skills":
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    com.html("""
            <div>
                <style>
                h1.heading {
                    background-color: #d33682;
                    color: white;
                    border-radius: 10px;
                    text-align: center;
                }
                </style>
                <h1 class="heading">Skills</h1>
                <p></p>
            </div>
            """, height=60)
    st.write(
        """
    - 👩‍💻 Python
    - 📊 Java
    - 📚 PHP
    - 👩‍💻 C/C++
    - 📊 Html
    - 📚 CSS
    - 🗄️ Databases: (MySQL, SQL Server)
    - 👩‍💻 Computer Vision (Hand tracking,Object detection,Face recognition,image processing
    - 📚 Hardware (Arduino,sensors,cameras)
    - 🚧 Frameworks/Libraries
    - 👩‍💻 Tensorflow
    - 📊 Opencv
    - 📚 cvzone
    - 🗄️ Hugging Face
    - 👩‍💻 Arduino Libraries


    """
    )
    st.write('---')

if selected == "Comp Vision Projects":
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    com.html("""
           <div>
               <style>
               h1.heading {
                   background-color: #d33682;
                   color: white;
                   border-radius: 10px;
                   text-align: center;
               }
               </style>
               <h1 class="heading">Computer Vision Projects</h1>
               <p></p>
           </div>
           """, height=60)

    st.write(
        """
    - ☀️ Helmet detection system using Custom Trained YOLO model
    - ☀️ Bag counter using Custom trained YOLO model
    - ☀️ Vehicle counting system using YOLO V8
    - ☀️ Person counting system using YOLO V8
    - ☀️ Bottle counting system on conveyor belt using YOLO V8
    - ☀️ Detecting and counting faces in images using YOLO V8
    - ☀️ Situp counter Posedetector from cvzone
    - ☀️ Pushup Counter using Posedetector from cvzone
    - ☀️ Hand gesture controlled lights using handtracking module from cvzone
    - ☀️ Hand detection and finger counter system
    - ☀️ Intelligent surveilliance camera 
    - ☀️ Face Recognition system 
    - ☀️ License plate detection system



    """
    )
    st.write('---')
    com.html("""
                           <div>
                               <style>
                               h1.heading {
                                   background-color: #d33682;
                                   color: white;
                                   border-radius: 10px;
                                   text-align: center;
                               }
                               </style>
                               <h1 class="heading">Computer Vision projects Gallery</h1>
                               <p></p>
                           </div>
                           """, height=60)
    st.write('\n')

    col1, col2 = st.columns(2)

    with col1:
        st.image("images/1.jpg", use_column_width=True, caption="Counting People in an image")
        st.image("images/2.jpg", use_column_width=True, caption="Push Up Counter")
        st.image("images/3.jpg", use_column_width=True, caption="Face Recognition System")

    with col2:
        st.image("images/4.jpg", use_column_width=True, caption="Bottle Counting System")
        st.image("images/5.jpg", use_column_width=True, caption="Vehicle classification and counting System")
        st.image("images/6.jpg", use_column_width=True, caption="Car Parking Space Counting System")

    st.write('---')

if selected == "Arduino Projects":
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    com.html("""
          <div>
              <style>
              h1.heading {
                  background-color: #d33682;
                  color: white;
                  border-radius: 10px;
                  text-align: center;
              }
              </style>
              <h1 class="heading">Arduino Projects</h1>
              <p></p>
          </div>
          """, height=60)

    st.write(
        """
    - ☀️ Voice controlled Robot
    - ☀️ Obstacle avoiding Robot using servo motor
    - ☀️ Line follower Robot
    - ☀️ Edge avoiding Robot
    - ☀️ Mobile app controlled Robot car using bluetooth module
    - ☀️ Surveiliance Camera car using ESP32 CAM
    - ☀️ Home light control using mobile app
    - ☀️ Automatic dustbin using ultrasonic sensor
    - ☀️ Smart stick for blind person
    - ☀️ Automatic water dispenswer
    - ☀️ Automatic room light system using PIR sensor
    - ☀️ Fire Alarm System





    """

    )
    com.html("""
                               <div>
                                   <style>
                                   h1.heading {
                                       background-color: #d33682;
                                       color: white;
                                       border-radius: 10px;
                                       text-align: center;
                                   }
                                   </style>
                                   <h1 class="heading">Arduino projects Gallery</h1>
                                   <p></p>
                               </div>
                               """, height=60)
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/7.jpg", use_column_width=True, caption="Voice Controlled Robot")
        st.image("images/8.jpg", use_column_width=True, caption="Obstacle Avoiding Robot Using Servo Motor")
        st.image("images/9.jpg", use_column_width=True, caption="Automatic Room Light")

    with col2:
        st.image("images/10.jpg", use_column_width=True, caption="Line Following Robot")
        st.image("images/11.jpg", use_column_width=True, caption="Android App Controlled Robot")
        st.image("images/12.jpg", use_column_width=True, caption="Smart Dustbin")
    st.write('---')

    # ---Machine Learning/Deep Learning/Streamlit Projects

    
if selected == "Deep Learning Projects":
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    com.html("""
             <div>
                 <style>
                 h1.heading {
                     background-color: #d33682;
                     color: white;
                     border-radius: 10px;
                     text-align: center;
                 }
                 </style>
                 <h1 class="heading">Machine Learning/Deep Learning/Streamlit Projects</h1>
                 <p></p>
             </div>
             """, height=60)

    st.write(
        """
    - ☀️ Digits classification using tensorflow and keras
    - ☀️ Cats and Dog classification using CNN
    - ☀️ Comment analyzer
    - ☀️ Portfolio website

    """
    )

if selected == "Comp Vision Games":
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    com.html("""
              <div>
                  <style>
                  h1.heading {
                      background-color: #d33682;
                      color: white;
                      border-radius: 10px;
                      text-align: center;
                  }
                  </style>
                  <h1 class="heading">Games using Computer Vision</h1>
                  <p></p>
              </div>
              """, height=60)

    st.write(
        """
    - ☀️ Balloon pop game using pygame hand tracking modle
    - ☀️ Snake game using pygame hand tracking module
    - ☀️ Eatable non eatable game using pygame
    - ☀️ Virtual Quiz game using pygame Hand Tracking Module
    - ☀️ Created executable (.exe) files for computer vision games
    - ☀️ Developed installers for computer vision games

    """
    )

    # --- TEACHING EXPERIENCE
    st.write('---')
if selected == "Teaching Experience":
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    com.html("""
                 <div>
                     <style>
                     h1.heading {
                         background-color: #d33682;
                         color: white;
                         border-radius: 10px;
                         text-align: center;
                     }
                     </style>
                     <h1 class="heading">Teaching Experience</h1>
                     <p></p>
                 </div>
                 """, height=60)

    st.write(
        """
    - ☀️ Taught intermediate students (ICS 2nd Year) various projects
    - ☀️ Computer Vision Projects (e.g., hand tracking, object detection)
    - ☀️ Arduino projects (e.g., robotics,automation)
    - ☀️ Developed and delivered curriculum materials, including tutorials and code exam.
    - ☀️ Mentored students in project development, debugging,and problem-solving


    """
    )
    com.html("""
                     <div>
                         <style>
                         h1.heading {
                             background-color: #d33682;
                             color: white;
                             border-radius: 10px;
                             text-align: center;
                         }
                         </style>
                         <h1 class="heading">Projects by my students (video links)</h1>
                         <p></p>
                     </div>
                     """, height=60)

    col1, col2 = st.columns(2)
    with col1:
        st.write("☀️☀️☀️Computer Vision Projects☀️☀️☀️")
        st.video("https://youtu.be/Gt4R4AsbeQg?feature=shared")

    with col2:
        st.write("☀️☀️☀️☀️☀️Arduino Projects☀️☀️☀️☀️")
        st.video("https://youtu.be/172nHbDjWnM?feature=shared")

if selected == "Israr's AI Bot":
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    com.html("""
                     <div>
                         <style>
                         h1.heading {
                             background-color: #d33682;
                             color: white;
                             border-radius: 10px;
                             text-align: center;
                         }
                         </style>
                         <h1 class="heading">Israr's AI Bot</h1>
                         <p></p>
                     </div>
                     """, height=60)
    st.write('\n')
    left_column, center_column, right_column = st.columns(3)
    with center_column:
        st.image("images/robo2.gif", use_column_width=True, caption="")

    user_question = st.text_input("Ask anything about me")
    st.write('\n')
    if st.button("ASK", use_container_width=True):
        persona = """
                        You are Israr Ahmad AI bot. You help people answer questions about yourself (i.e. ISRAR).
                        Answer as if you are responding. Don't answer in second or third person.
                        If you don't know the answer, you simply say "That's a secret".
                        Here is more info about Israr Ahmad:
                        ISRAR AHMAD is an educator, computer vision application developer, Arduino project developer, and web developer with a keen interest in learning new technologies.I have created various Arduino robot cars, including line-following, obstacle-avoiding, edge-avoiding, and voice-controlled robot cars. Additionally, I have developed several computer vision projects using OpenCV, such as a bottle counting system, vehicle counting system, bags counting system on a conveyor belt using custom-trained models, person counting system using YOLO model, license plate detection system, hand-controlled light, helmet detection system using custom-trained models, intelligent surveillance camera, and eye blink counter system.I have also created a digits classification system using TensorFlow and Keras, a dogs and cats image classification system using CNN, and a portfolio website using Streamlit.I charge for projects depending on the type, nature, and complexity of the project, as well as the number of live sessions required for debugging. I live in Layyah district, Punjab province, Pakistan.Israr Ahmad obtained his M.Phil degree in Computer Science and has extensive experience in the fields of Arduino and computer vision, later specializing in robotics.I have also worked as a software developer.

    He also has skills in programming languages such as Python, PHP, Java, WordPress, Streamlit, HTML, CSS, and databases like MySQL and SQL Server. He has developed interesting educational games using computer vision and Pygame. He has more than 12 years of teaching experience and 5 years of experience in developing Arduino projects.He does not have a YouTube channel but can be contacted via email at azlanshly@gmail.com.He explores different sources to learn technology, such as ChatGPT, Stack Overflow, Google AI Bard, YouTube, various blogs, and websites. He learned Arduino by doing experiments and from the website arduino.cc.
    He also has two years of experience in web development. He has developed various websites, such as an online voting system, an online complaint management system, an online mobile shop, and an online watch sales platform. Additionally, he created a comment analyzer using Streamlit and Hugging Face, and worked on sentiment analysis. He also developed a face recognition system using computer vision.
    For Arduino projects, he used Arduino Uno, Arduino SMD, and Arduino Nano.
    I do not charge for projects for students.
    I am lucky to have had so many teachers who changed my life. They are all the best, but in the field of computer vision, Sir Murtaza Hassan is my favorite teacher.




                        Israr's Email: azlanshly@gmail.com 

                        """
        prompt = persona + "Here is the question that the user asked: " + user_question
        response = model.generate_content(prompt)
        st.write(response.text)
        st.write("\n")
    st.write('##')
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write('---')
if selected == "Contact":
    st.header("Reach out to me at!!")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
        <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

            # lottie_coding = load_lottiefile("lottiefile.json")  # replace link to local lottie file


        # lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")
        lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_lt8ter7g.json")

        st_lottie(
            lottie_hello,
            speed=1,
            reverse=True,
            loop=True,
            quality="low",  # medium ; high
            renderer="svg",  # canvas
            height=None,
            width=None,
            key=None,
        )
        st.write('---')
