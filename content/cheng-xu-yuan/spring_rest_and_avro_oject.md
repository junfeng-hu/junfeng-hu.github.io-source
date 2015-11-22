Title: Spring Rest server and Apache Avro objects
Date: 2015-08-07 16:58:57
Author: junfeng
Category: 程序猿
Tags: Spring, Rest, Avro

###1. Error handle class
```java
@ControllerAdvice
public class ErrorHandler {
    @ExceptionHandler(value = Exception.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    @ResponseBody
    public ErrorResponse errorResponse(Exception exception) {
        return exception.getMessage();
    }
}
```

then we can got clear error message
####Reference
[http://www.importnew.com/7903.html][4]

###2. Change response's content-type
```java
@RequestMapping(method = RequestMethod.GET, produces = MediaType.APPLICATION_JSON_VALUE)
```
need for just return JSON string

####Reference
[http://stackoverflow.com/questions/4471584/in-spring-mvc-how-can-i-set-the-mime-type-header-when-using-responsebody][1]

###3. Customize `MappingJackson2HttpMessageConverter`'s behaviors
```java
@Bean
public Jackson2ObjectMapperBuilder objectMapperBuilder() {
    Jackson2ObjectMapperBuilder builder = new Jackson2ObjectMapperBuilder();
    // configure ObjectMapper here
    //builder.serializationInclusion(JsonInclude.Include.NON_NULL);
    builder.featuresToEnable(MapperFeature.REQUIRE_SETTERS_FOR_GETTERS);
    return builder;
}
```

add the above code snippet to any of your Configuration classes
####Reference
[http://stackoverflow.com/questions/28324352/how-to-customise-the-jackson-json-mapper-implicitly-used-by-spring-boot][2]

###4. Let Spring `@RestController` gives Avro objects a hug
make Avro generated class objects automatically converted to JSON string by
`MappingJackson2HttpMessageConverter`

Two methods:

1. `avro_object.toStirng()` and change response's content-type to application/json
2. configure `MapperFeature.REQUIRE_SETTERS_FOR_GETTERS` to `true`
   for Jackson's `ObjectMapper`, use the method at above section.

####References
[https://github.com/FasterXML/jackson-dataformat-avro/issues/16][3]

[1]: http://stackoverflow.com/questions/4471584/in-spring-mvc-how-can-i-set-the-mime-type-header-when-using-responsebody
[2]: http://stackoverflow.com/questions/28324352/how-to-customise-the-jackson-json-mapper-implicitly-used-by-spring-boot
[3]: https://github.com/FasterXML/jackson-dataformat-avro/issues/16
[4]: http://www.importnew.com/7903.html
