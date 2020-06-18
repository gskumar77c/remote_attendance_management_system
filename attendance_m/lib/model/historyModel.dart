import '../component/jason_prac.dart';
import '../component/general_classes.dart';

String subjectId = "";
String studentId = "";
String message = "";
// Default Radio Button Selected Item.
String radioItemHolder = 'All';
// Group Value for Radio Button.
int groupId = 1;
String chosenStudentId = "";
List<Subject> subjectList;
List<StudentClass> studentList;
List<NumberList> nList = [
  NumberList(
    index: 1,
    type: "All",
  ),
  NumberList(
    index: 2,
    type: "Limited",
  ),
];

bool validateEntry() {
  print(subjectId);
  print(groupId);
  print(Dates.startDate);
  print(Dates.endDate);
  if (subjectId != "") {
    if (groupId == 2 && (Dates.startDate == null || Dates.endDate == null)) {
      message = "select start and end date, both !";
      return false;
    } else {
      return true;
    }
  } else {
    message = "select a subject, both !";
    return false;
  }
}
