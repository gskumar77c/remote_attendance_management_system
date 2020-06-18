import 'dart:io';

class SharedList {
  static List<File> resultList;

  static add(File value) {
    resultList = List<File>();
    resultList.add(value);
  }
}
