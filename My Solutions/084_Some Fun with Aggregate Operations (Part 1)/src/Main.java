import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        // Buat objek student
        Student student1 = new Student("Beno", 98, "Computer Science", Student.Gender.MALE);
        Student student2 = new Student("Jeny", 80, "Fashion", Student.Gender.FEMALE);
        Student student3 = new Student("Rose", 78, "Fashion", Student.Gender.FEMALE);
        Student student4 = new Student("Alice", 90, "Computer Science", Student.Gender.MALE);

        // Membuat stream dari objek Student
        Stream<Student> studentStream = Stream.of(student1, student2, student3, student4);

        // Memanggil metode getAverageGradeByDepartment
        Map<String, Double> averageGradesByDepartment = AggregationKata.getAverageGradeByDepartment(studentStream);

        // Menampilkan hasil
        averageGradesByDepartment.forEach((department, averageGrade) ->
                System.out.println("Department: " + department + ", Average Grade: " + averageGrade));

    }
}
