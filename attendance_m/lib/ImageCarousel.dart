import 'dart:ui'; 

import 'punch_att.dart';  
import 'package:flutter/material.dart';  





class ImageCarousel extends StatefulWidget {  
  ImageCarousel();
  _ImageCarouselState createState() => new _ImageCarouselState();
}

class _ImageCarouselState extends State<ImageCarousel> with SingleTickerProviderStateMixin {
  _ImageCarouselState();

  Animation<double> animation;
  AnimationController controller;

  initState() {
    super.initState();
    controller = new AnimationController(
        duration: const Duration(milliseconds: 2000), vsync: this);
    animation = new Tween(begin: 0.0, end: 18.0).animate(controller)
      ..addListener(() {
        setState(() {
          // the state that has changed here is the animation object’s value
        });
      });
    controller.forward();
  }

  @override
  Widget build(BuildContext context) { 

    return new Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        title: Text(
          'Selected Images'
        ),
      ),
      body: new Center(
        child:    ListView.builder(
              scrollDirection: Axis.horizontal,
              itemCount: shared_list.resultList.length,
              itemBuilder: (context,c)
              {

                return Card(
                  child: Image.file(shared_list.resultList[c],
                    fit: BoxFit.fill,
                    width: 400,
                    height: 400,

                  ),
                );
              }
          ),
      
      ),
    );
  }

  dispose() {
    controller.dispose();
    super.dispose();
  }
}