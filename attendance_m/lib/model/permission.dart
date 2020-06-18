import 'package:shared_preferences/shared_preferences.dart';

checkLoginStatus(SharedPreferences sharedPreferences) async {
  sharedPreferences = await SharedPreferences.getInstance();
}