package kr.hwaner.spring.hint;

import org.h2.server.web.WebServlet;
import org.springframework.boot.web.servlet.ServletRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @author hwaner
 */
@Configuration
public class DatabaseConfig {

    @Bean
    public ServletRegistrationBean h2servletRegistration() {

        ServletRegistrationBean registration = new ServletRegistrationBean(new WebServlet());
        registration.addUrlMappings("/console/*");
        return registration;
    }
}
