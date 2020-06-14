# Crack Top Android Development Company Interview

[link to Google!](https://docs.google.com/document/d/1H0jRY8oKAFpE8sT_hHjiUmvEZYJFx8IXqzoNB2su-ao/edit?usp=sharing)
Budhdi Sharma
May 8 · 15 min read


The interviewer in interviews asked these questions with top-tier Internet companies. Familiarity with the knowledge points listed in this article will greatly increase the chance of passing the first two rounds of technical interviews.
Mainly divided into the following parts:
* (1) Java interview questions
* (2) Android interview questions
* (3) Advanced development technology interview questions
* (4) Cross-platform Hybrid development

## Java interview questions
Mastering java is very important. Large companies not only require you to use a few APIs, but also require you to be familiar with the principles of source code implementation, and even require you to know what are the deficiencies, how to improve, and some Java-related algorithms, Design patterns, etc.
### Java basic interview knowledge points
- The difference between == and equals and hashCode in java
- How many bytes each int, char, and long occupy
- The difference between int and integer
- Explore the understanding of java polymorphism
- Difference between String, StringBuffer, StringBuilder
- What is the internal class? The role of inner classes
- The difference between abstract classes and interfaces
- The meaning of abstract class
- Application scenarios of abstract classes and interfaces
- Can abstract classes have no methods and properties?
- The meaning of the interface
- The difference between extends and super in generics
- Can the child class override the static method of the parent class?
- The difference between process and thread
- The difference between final, finally, and finalize
- Serialization
- The difference between Serializable and Parcelable
- Can static properties and static methods be inherited? Can it be rewritten? And why?
- Design Intent of Static Inner Class
- Understanding of member internal class, static internal class, local internal class, and anonymous internal class, and application in the project
- Talk about understanding kotlin
- The difference between closures and local inner classes
- The method and principle of converting the string to integer
## Java in-depth source-level interview questions (difficult)
Under what circumstances will the object be disposed of by the garbage collection mechanism?  
Tell me about common coding methods?  
How many bytes does English in UTF-8 encoding take; how many bytes is int?  
What is the difference between static proxy and dynamic proxy?  
Java’s exception system  
Talk about your understanding of parsing and assignment.  
Modify the signature of the equals method of object A, so which equals method will be called when using HashMap to store this object instance?  
What is the mechanism for implementing polymorphism in Java?  
How to serialize a Java object into a file?  
Talk about your understanding of Java reflection  
Talk about your understanding of Java annotations  
Talk about your understanding of dependency injection  
Talk about the principle of generics and give examples  
Understanding of String in Java  
Why should String be designed to be immutable?  
Object equal and hashCode method rewrite, why?  

## Data structure
Introduction to common data structures  
What does concurrent collection know?  
List Java collections and the inheritance relationship between collections  
Collection class and collection framework  
Introduction to the container class and the difference between them (the container class is estimated that many people do not listen to this term. Java containers can be divided into four parts: List list, Set collection, Map mapping, and tool class (Iterator iterator, Enumeration enumeration class Arrays and Collections)  
The difference between List, Set, Map  
List and Map implementation and storage  
The realization principle of HashMap  
HashMap data structure?  
HashMap source code understanding  
How to put data in HashMap (explain from the perspective of HashMap source code)?  
How to implement HashMap by hand?  
Implementation principle of ConcurrentHashMap  
Comparison of ArrayMap and HashMap  
HashTable implementation principle  
TreeMap implementation  
The difference between HashMap and HashTable  
The difference between HashMap and HashSet  
How do HashSet and HashMap judge duplicate elements in a set?  
How does Set prevent Hash to prevent collision?  
The difference between ArrayList and LinkedList, and application scenarios  
The difference between arrays and linked lists  
Concrete implementation of depth-first traversal and breadth-first traversal of binary trees  
The structure of the heap  
The difference between heap and tree  
What is the difference between heap and stack in memory (answer hint: you can answer from two aspects of data structure and actual implementation)?  
What is deep copy and shallow copy  
Handwritten linked list reverse order code  
Tell me about the understanding of trees, B + trees  
Tell me about the understanding of the picture  
To judge whether a singly linked list is looped?  
Linked list flip (ie: flip a single necklace watch)  
Merging multiple single-ordered linked lists (assuming all are increasing)  

## Threads, multithreading and thread pool
Three ways to start threads?  
The difference between threads and processes?  
Why are there threads, not just processes?  
The difference between run () and start () methods  
How to control the number of concurrent access threads for a method?  
The difference between wait and sleep() methods in Java;  
Talk about the understanding of the wait / notify keyword  
What causes the thread to block?  
How do threads close?  
Tell me about the synchronization method in java  
How to ensure data consistency?  
How to ensure thread safety?  
How to achieve thread synchronization?  
Can both processes write or read at the same time? How to prevent process synchronization?  
Inter-thread operation List  
Life cycle of objects in Java  
Synchronized usage  
Principle of synchronize  
Talk about the understanding of Synchronized keywords, class locks, method locks, reentrant locks  
Multi-threaded access and function of static synchronized method  
Two synchronized methods in the same class, the problem of simultaneous access by two threads  
The principle of volatile  
Talk about the usage of volatile keyword  
Talk about the role of the volatile keyword  
Talk about NIO’s understanding  
The difference between synchronized and volatile keywords  
The difference between synchronized and Lock  
ReentrantLock, synchronized and volatile comparison  
ReentrantLock’s internal implementation  
lock principle  
The four necessary conditions for deadlock?  
How to avoid deadlock?  
Will object locks and class locks affect each other?  
What is a thread pool and how to use it?  
Java’s concurrency, multithreading, threading model  
Talk about the understanding of multi-threading  
What are the issues to be aware of in multithreading?  
Talk about your understanding of concurrent programming and give examples  
Talk about your understanding of the multi-thread synchronization mechanism?  
How to ensure the security of multi-threaded read and write files?  
Multithread breakpoint resume transmission principle  
Realization of resuming of breakpoint  
### Knowledge points about concurrent programming
Usually, less concurrent programming can be done in Android development. The Thread class is often used, but if we want to improve ourselves, we must not stay on the surface. We should also learn about java’s thread-related source code thing.

## Android interview questions
Android interview questions include Android basics, as well as some source-level, principle, etc. So if you want to go to an interview with a large company, you must look at the source code and implementation methods. Common frameworks can try whether you can implement it by hand and exercise yourself.
### Android basics
What are the four components?  
The life cycle and simple usage of the four major components  
Communication between activities  
Activity life cycle under various circumstances  
When switching between horizontal and vertical screens, the life cycle of Activity in various situations  
Life cycle comparison between Activity and Fragment  
Life cycle when pressing the Home button when there is a Dialog on the Activity  
Which methods must be executed when jumping between two activities?  
The foreground switches to the background, and then back to the foreground, Activity life cycle callback method. Dialog pops up, life cycle callback method.  
Comparison of the four startup modes of Activity  
Activity state saved in recovery  
Fragment life cycle in various situations  
Fragment state save startActivityForResult is which class method, under what circumstances?  
How to realize the sliding of Fragment?  
How to transfer data between fragments?  
How does Activity bind to Service?  
How to start the corresponding Service in Activity?  
How to perform data interaction between service and activity?  
Service opening method  
Please describe the life cycle of Service  
Talk about your understanding of ContentProvider  
Talk about the relationship between ContentProvider, ContentResolver, ContentObserver  
Please describe the understanding of BroadcastReceiver  
Broadcast classification  
Ways and scenarios of broadcast use  
How to register and use BroadcastReceiver in the manifest and code?  
What is the difference between local broadcast and global broadcast?  
BroadcastReceiver, LocalBroadcastReceiver difference  
AlertDialog, popupwindow, activity difference  
The difference between Application and Activity Context objects  
Android property animation features  
How to import an external database?  
Features and comparison of LinearLayout, RelativeLayout, and FrameLayout, and introduces usage scenarios.  
Talk about the understanding of interfaces and callbacks  
The principle of callback  
Write a callback demo  
Introduction to SurfView  
Use of RecycleView  
The role of serialization, and the difference between the two serialization of Android  
Difference  
Estimator  
How to store data in Android  
### Android source code related analysis
Android animation framework implementation principle  
Differences between APIs of Android versions  
Requestlayout, onlayout, onDraw, DrawChild difference and connection  
The difference and use of invalidate and postInvalidate  
The difference between Activity-Window-View  
Talk about understanding Volley  
How to optimize custom View  
How does the low version SDK implement the high version API?  
Describe the flow of a network request  
HttpUrlConnection and okhttp relationship  
Understanding Bitmap objects  
looper architecture  
The working principle of ActivityThread, AMS, WMS  
Custom View how to consider model adaptation  
Custom View events  
What is the difference between AstncTask + HttpClient and AsyncHttpClient?  
LaunchMode application scenarios  
How to use AsyncTask?  
SpareArray principle  
Please introduce how ContentProvider implements data sharing?  
Several ways of communication between AndroidService and Activity  
What is the principle and role of IntentService?  
Talk about the relationship between Activity, Intent, Service  
The difference between ApplicationContext and ActivityContext  
Is SP synchronized by process? Is there any way to achieve synchronization?  
Talk about the use of multi-threading in Android  
Process and Application Life Cycle  
How to know the size of the view when packaging the view  
RecycleView principle  
The role and understanding of AndroidManifest  
## Some common principle problems
Handler mechanism and underlying implementation  
The difference between Handler, Thread and HandlerThread  
How does the looper start when the handler sends a message to the child thread?  
Regarding Handler, what thread is the new Handler in any place?  
ThreadLocal principle, implementation and how to ensure the Local property?  
Please explain the relationship between Message, Handler, Message Queue, Looper in the single-threaded model  
Please describe the View event delivery and distribution mechanism  
Touch event delivery process  
What is the difference between onTouch and onTouchEvent in event distribution, and how to use it?  
What are the callback methods related to event distribution in View and ViewGroup?  
View refresh mechanism  
View drawing process  
Principle of custom control  
How does a custom View provide an interface to get View properties?  
Implement WAP networking in Android code  
AsyncTask mechanism  
AsyncTask principle and shortcomings  
How to cancel AsyncTask?  
Why can’t I update the UI on the child thread?  
What is the cause of ANR?  
ANR positioning and correction  
What is oom?  
What causes oom?  
Is there any solution to avoid OOM?  
Can Oom try catch? why?  
What is a memory leak?  
What causes a memory leak?  
How to prevent memory leaks of threads?  
Solution for memory leak field  
Difference between memory leak and memory overflow?  
LruCache default cache size  
ContentProvider permission management (answer: read-write separation, permission control-accurate to table level, URL control)  
How to intercept and abort a text message through broadcast?  
Can broadcast request network?  
What is the time limit of anr caused by broadcasting?  
Calculate the nesting level of a view  
Activity stack  
Is there an upper limit for Android threads?  
Is there an upper limit for the thread pool?  
What does ListView reuse?  
Why did Android introduce Parcelable?  
Have you tried to simplify the use of Parcelable  
### Some common problems in the development
How does the problem of image misalignment in ListView arise?  
Do you understand hybrid development?  
Know which hybrid development methods? Name their advantages and disadvantages and their respective usage scenarios? (Answer: For example RN, weex, H5, applet, WPA, etc. It is still beneficial to do some understanding of Android-front-end js, etc.);  
What are the processing techniques for screen adaptation?  
The server only provides a data receiving interface. How to ensure the orderly arrival of data under multi-thread or multi-process conditions?  
Understanding dynamic layout  
How to remove duplicate code?  
Draw the general architecture diagram of Android  
The difference between Recycleview and ListView  
The principle and solution of ListView image loading disorder  
Dynamic permission adaptation scheme, the concept of the permission group  
Why did the Android system design ContentProvider?  
Does the drop-down status bar affect the life cycle of the activity  
If a network request is made during onStop, how to recover it during onResume?  
What should you pay attention to when using Bitmap?  
Bitmap recycler ()  
The main steps to turn on the camera in Android  
ViewPager usage details, how to set it to initialize the current Fragment every time, other not initialized?  
Click event is intercepted, but want to pass to the View below, how to operate?  
Implementation of WeChat main page  
The principle of the little red dot on the WeChat message  
Introduction to CAS  

# Advanced development technology interview questions
Here are some high-end Android technologies that large companies need to use. Here I have compiled a document specifically; I hope everyone can look. These topics are a bit technical and need some time to study.
### Picture
Picture library comparison  
Source analysis of image library  
Picture frame cache implementation  
Principle of LRUCache  
Image loading principle  
How to do it by yourself to realize the picture library?  
Glide source code analysis  
What cache does Glide use?  
How to control the size of Glide memory cache?  
### Network and security mechanisms  
Network framework comparison and source code analysis  
How to do it yourself to design a network request framework?  
okhttp source code  
Network request cache processing, how does okhttp handle network cache  
Load a 10M picture from the network and talk about the precautions  
TCP’s 3 handshake and 4 waves  
The difference between TCP and UDP  
Application of TCP and UDP  
HTTP protocol  
The difference between HTTP1.0 and 2.0  
HTTP message structure  
The difference between HTTP and HTTPS and how to achieve security  
How to verify the validity of the certificate?  
Where is symmetric encryption used in https, and where is asymmetric encryption used? Do you know the encryption algorithm (such as RSA)?  
How does the client determine that the message it sent was received by the server?  
Talk about your understanding of WebSocket  
The difference between WebSocket and socket  
Talk about your understanding of Android signature.  
Please explain why Android needs to add a signature mechanism?  
Video encryption transmission  
How are apps sandboxed, and why do they do it?  
Permission management system (how is the bottom permission granted)?  
### Database
sqlite upgrade, add field statement  
Database framework comparison and source code analysis  
Database optimization  
Database data migration issues  
### Algorithm
What are the sorting algorithms?  
What is the fastest sorting algorithm?  
Handwriting a bubble sort  
Handwritten quick sort code  
Quick sorting process, time complexity, space complexity  
Handwriting heap sorting  
Heap sorting process, time complexity and space complexity  
Write the sorting algorithm you know, time-space complexity, stability  
Binary tree gives root node and target node, find the path from root node to target node  
Which algorithm should be selected for sorting by age for more than 20,000 employees of Ali?  
GC algorithm (the advantages and disadvantages of various algorithms and application scenarios)  
Ant colony algorithm and Monte Carlo algorithm  
Substring inclusion problem (KMP algorithm) write code implementation  
An unordered, non-repetitive array outputs N elements, so that the sum of N elements is added as M, giving time complexity and space complexity. Handwriting algorithm  
Trillion-level two URL files A and B. How to find the difference C between A and B optimization)  
How to try to find the nearest merchant function in Baidu POI (hint: coordinate mirror + R tree).  
Find the common elements in two non-repeating array collections.  
Of the two non-repeating array collections, these two collections are huge amounts of data, which cannot be put in memory. How to find common elements?  
There are 1 million integers in a file, separated by spaces. In the program, determine whether the integer entered by the user is in this file. Say the best way  
Calculation of memory occupied by a Bitmap and memory usage  
20 million integers, find the 50th largest number?  
It takes a total of 1 hour to burn an uneven rope from start to finish. Now that there are several ropes of the same material, how do you use the method of burning rope to time an hour and fifteen minutes?  
Find the number of daffodils within 1,000 and the number of daffodils within 4 billion  
How to divide 5 coins, 2 positives and 3 negatives into two piles, and then turn over to make the number of hard 8 coins facing upwards and the number of coins facing upwards in the two piles the same  
The hour hand goes one turn, the hour hand and minute hand overlap several times  
N * N graph paper, how many squares are inside  
X apples can only eat one, two, or three a day. How many days can I finish?  
### Plug-in, modularization, componentization, hot repair, incremental update, Gradle
Understanding of hot repair and plug-in  
Analysis of plug-in principle  
Modular implementation (benefits, reasons)  
Hot fix, plug-in  
Project component understanding  
Describe what happened after clicking the build button of Android Studio  
### Architecture design and design mode  
Talk about your understanding of the Android design pattern  
MVC MVP MVVM principle and difference  
What design patterns do you know?  
Design patterns commonly used in projects  
Handwritten producer / consumer model  
Write the code for the observer mode  
Similarities and differences between adapter mode, decorator mode, and appearance mode?  
Some open source frameworks used, introduce an internal implementation process that has seen the source code.  
Talk about understanding RxJava  
RxJava function and principle realization  
The advantages and disadvantages of the role of RxJava compared with the asynchronous operations usually used  
Talk about the function and implementation of EventBus, the way to replace EventBus  
Design an overall app architecture from 0, how to do it?  
Say and design an application that you think is currently hot (for example: live broadcast app, P2P finance, small video, etc.)  
Talk about understanding the java state machine  
How to decouple if Fragment is used in Adapter?  
Binder mechanism and its underlying implementation  
How does this update work for apps? (Answer: Grayscale, mandatory update, update by area)?  
Implement a Json parser (can increase speed through regularization)  
Statistics start time, standard  

## Performance optimization
How to perform performance analysis and optimization of Android applications?  
ddms and traceView  
How to analyze systrace for performance optimization?  
How to analyze memory leak with IDE?  
How to solve the performance problem caused by Java multithreading?  
Start screen white screen and black screen solved?  
How to solve the problem of too slow startup?  
How to ensure that the application does not freeze?  
App startup crash exception capture  
Notes on customizing View  
Now the download speed is very slow, try to analyze the reason from the perspective of the network protocol and optimize it (hint: all 5 layers of the network can be involved).  
Https request slow solution (hint: DNS, carry data, directly access IP)  
How to maintain the stability of the application  
RecyclerView and ListView performance comparison  
ListView optimization  
RecycleView optimization  
View rendering  
How does Bitmap handle big pictures, such as a 30M big picture, how to prevent OOM  
The difference between the four kinds of references in java and usage scenarios  
Will the strong reference be set to null, will it be recycled?  

## NDK, jni, Binder, AIDL, process communication
Please introduce NDK  
What is the NDK library?  
Have you used jni?  
How to register native function in jni, there are several ways to register?  
How does Java call C and C ++ languages?  
How does jni call java layer code?  
How to communicate between processes?  
Binder mechanism  
Brief description of IPC?  
What is AIDL?  
What problem does AIDL solve?  
How to use AIDL?  
How does Inter-Process-Communication work on Android?  
Have you met a multi-process scenario?  
Android process classification?  
Process and Application life cycle?  
Process scheduling  
Talk about the understanding of process sharing and thread safety  
Talk about the understanding of multi-process development and multi-process application scenarios  
What is a coroutine?  

## Framework layer, ROM customization, Ubuntu, Linux, and other issues
Characteristics of java virtual machine  
Talk about the understanding of jvm  
JVM memory area, which memory is affected by threading  
What do you know about Dalvik and ART virtual machines?  
Art and Dalvik comparison  
The principle of virtual machine, how to design a virtual machine yourself (memory management, class loading, parent delegation)  
Talk about your understanding of the parent delegation model  
JVM memory model, memory area  
Classloading mechanism  
Talk about the understanding of ClassLoader (class loader)  
Talk about the understanding of dynamic loading (OSGI)  
Circular references and avoidance of memory objects  
Memory recycling mechanism, GC recycling strategy, GC timing, and GC objects  
The difference between the garbage collection mechanism and calling System.gc ()  
Ubuntu compile Android system  
What is the system startup process? (Hint: Zygote process-> SystemServer process-> various system services-> application process)  
Generally speaking, what happens when an application is installed on the phone  
Briefly describe the entire process of Activity startup  
App startup process, start by clicking on the desktop  
Logical address and physical address, why use logical address?  
What is the amount of memory allocated by Android for each application?  
Can Android allocate process memory by itself?  
Process keep alive  
How to ensure that a background service is not killed? (Same question: How to ensure that the service is not killed in the background?)   What is the more power-saving way?  
How to wake up other processes in the app  

## Cross-platform Hybrid development
flutter  
Html5 project combat  
HTML & CSS & JavaScript combat  
WordPress building website project combat  
Front-end Vue architecture  
Front-end style development  
Weex built-in capabilities  
Weex native application  
Weex extension framework  
WeexUI architecture  
Introduce which projects you have done  
What frameworks and platforms have you used?  
What custom controls have you used?  
What are the areas where the research is more in-depth?  
What are the channels of concern for industry information?  
What books have you read recently?  
Are there any open source projects?  
The technical points that I am most good at, the technical fields and technical points that I am most interested in
What open source libraries are used in the project and how to avoid the security and stability problems caused by the introduction of open-source libraries  
What did you do during the internship and what was your output?  

## Summary
Because the workload of sorting answers to many questions is too large, it is limited to providing knowledge points. If you are looking for a job, it is recommended to go through them one by one. If you do n’t understand, you can ask questions.  
I will write some more article/blog on Coding Interview Tips to get to know more about it, please follow or Clapp for the article.  
I hope you enjoyed this session. If you have any comments or questions, please join the forum discussion below!  
Thanks for the support :)  
[Android Developers](https://medium.com/u/e1f26db83092?source=post_page-----f106756f045e----------------------)
[Interviewstreet](https://medium.com/u/495e4a6d13a5?source=post_page-----f106756f045e----------------------)
[Crack Code Interview](https://medium.com/u/cadf9a318872?source=post_page-----f106756f045e----------------------)
$A \cup B$
$A \cap B$
