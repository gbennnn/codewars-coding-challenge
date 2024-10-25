/*
Codewars Coding Challenge

Day 84/366

Level 6kyu Java

Some Fun with Aggregate Operations (Part 1)

Problem: My Solutions\084_Some Fun with Aggregate Operations (Part 1)\problem\problem.txt


import java.util.stream.Stream;
import java.util.Map;

public class AggregationKata {

    public static Map<String, Double> getAverageGradeByDepartment(Stream<Student> students) {


    }

}


https://www.codewars.com/kata/595fa01cde9d341e8c000045/train/java

import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class AggregationKata {

    public static Map<String, Double> getAverageGradeByDepartment(Stream<Student> students) {
        return students.collect(Collectors.groupingBy(Student::getDepartment, 
                                                      Collectors.averagingDouble(Student::getGrade)));
    }

}

 */

import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class AggregationKata {
    public static Map<String, Double> getAverageGradeByDepartment(Stream<Student> students){
        return students.collect(Collectors.groupingBy(Student::getDepartment, Collectors.averagingDouble(Student::getGrade)));
    }
}
