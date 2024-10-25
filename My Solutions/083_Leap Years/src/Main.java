public class Main {
    public static void main(String[] args) {
        // Test Cases
        System.out.println(LeapYears.isLeapYear(2020)); // true : tahun kabisat
        System.out.println(LeapYears.isLeapYear(2000)); // true : tahun kabisat
        System.out.println(LeapYears.isLeapYear(2015)); // false : bukan tahun kabisat
        System.out.println(LeapYears.isLeapYear(2100)); // false : bukan tahun kabisat
    }
}
