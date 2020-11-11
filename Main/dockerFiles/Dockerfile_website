FROM ubuntu

ENV TZ=Asia/Jerusalem 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone 

RUN apt update
RUN apt install apache2 -y 
RUN apt install apache2-utils -y
RUN apt clean 
EXPOSE 80 
CMD ["apache2ctl", "-D", "FOREGROUND"]
