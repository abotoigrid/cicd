FROM openjdk:17-jdk-alpine  
WORKDIR /app               
COPY spring-petclinic*.jar app.jar  
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]  