import 'dart:convert';
 

  class teacher_details{
      static String name; 
      // static String enail; 
      static String id; 
      static List<subject_wise_detail> subject_detail_list; 
  }
  class subject_wise_detail
  {
    String subject_name;
    String subject_id;
    List<student_class>   students_list;
    subject_wise_detail(this.subject_name, this.subject_id , this. students_list);
  }
  class student_class
  {
    String student_name ;
    String student_id ;
    student_class(this.student_name, this.student_id);
  }

  class subject
  {
    String sub_name;
    String sub_id;
    subject(this.sub_id,this.sub_name);
  }

  
  class class_hist_date_wise {
      static List<date_attendance> attendence_list;
  }
  class date_attendance {
    String date;
    int  class_position_day;  ///use ful in case of multiple classes
    String present;
    String total; 

    date_attendance(this.date, this.class_position_day,this.present, this.total);
  }


  class student_hist {
    static String  course_id;
    static String  course_name;
    static String  student_id;
    static String  student_name;
    static List <student_daily_entry> attendence_list; 
  }
  class student_daily_entry {
    DateTime date;
    int  class_position_day; 
    bool attendance;
    student_daily_entry(this.date, this.class_position_day ,this.attendance);
  }

 


