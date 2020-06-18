import 'dart:convert';

class TeacherDetails {
  static String name;

  // static String email;
  static String id;
  static List<SubjectWiseDetail> subjectDetailList;
}

class SubjectWiseDetail {
  String subjectName;
  String subjectId;
  List<StudentClass> studentsList;

  SubjectWiseDetail(this.subjectName, this.subjectId, this.studentsList);
}

class StudentClass {
  String studentName;

  String studentId;

  StudentClass(this.studentName, this.studentId);
}

class Subject {
  String subName;
  String subId;

  Subject(this.subId, this.subName);
}

class ClassHistDateWise {
  static String subjectId = "";
  static List<DateAttendance> attendanceList;
}

class DateAttendance {
  String date;
  String slot;

  ///use ful in case of multiple classes
  String extraClass;

  ///use ful in case of multiple classes
  String present;
  String total;

  DateAttendance(
      this.date, this.slot, this.extraClass, this.present, this.total);
}

class StudentHist {
  static String courseId;
  static String courseName;
  static String studentId;
  static String studentName;
  static List<StudentDailyEntry> attendanceList;
}

class StudentDailyEntry {
  DateTime date;
  String slot;
  String extraClass;
  String attendance;

  StudentDailyEntry(this.date, this.slot, this.extraClass, this.attendance);
}
