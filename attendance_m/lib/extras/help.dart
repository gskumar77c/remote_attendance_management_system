// import 'package:flutter/material.dart';
// class LocationDetail extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text('Location Detail'),
//       ),
//       body: Column(
//           mainAxisAlignment: MainAxisAlignment.start,
//           crossAxisAlignment: CrossAxisAlignment.stretch,
//           children: [
//             ImageBanner("assets/images/kiyomizu-dera.jpg"),
//             TextSection(Colors.red),
//             TextSection(Colors.green),
//             TextSection(Colors.blue),
//           ]),
//     );
//   }
// }

// class TextSection extends StatelessWidget {
//   final Color _color;

//   TextSection(this._color);

//   @override
//   Widget build(BuildContext context) {
//     return Container(
//       decoration: BoxDecoration(
//         color: _color,
//       ),
//       child: Text('hi'),
//     );
//   }
// }

// class ImageBanner extends StatelessWidget {
//   final String _assetPath;

//   ImageBanner(this._assetPath);

//   @override
//   Widget build(BuildContext context) {
//     return Container(
//         constraints: BoxConstraints.expand(height: 200.0),
//         decoration: BoxDecoration(color: Colors.grey),
//         child: Image.asset(
//           _assetPath,
//           fit: BoxFit.cover,
//         ));
//   }
// }

// const String FontNameDefault = 'Montserrat';

// const Body1Style = TextStyle(
//   fontFamily: FontNameDefault,
//   fontWeight: FontWeight.w300,
//   fontSize: 26.0,
//   color: Colors.black,
// );

// style: TextStyle(fontWeight: FontWeight.bold);

// color: Theme.of(context).primaryColor =>>raisebutton;

// TextField(
//     decoration: InputDecoration(labelText: 'Amount'),
//     controller: _amountController,
//     keyboardType: TextInputType.numberWithOptions(decimal: true),
//     onSubmitted: (_) => _submitData(),
//     ),

//  crossAxisAlignment: CrossAxisAlignment.end,

// //Scaffold
//   body: SingleChildScrollView(
//         child: Column(
//           crossAxisAlignment: CrossAxisAlignment.stretch,
//           children: <Widget>[
//             TransactionList(this._userTransactions, this._deleteTransaction),
//           ],
//         ),
//       ),
//       floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,

//       floatingActionButton: FloatingActionButton(child: Icon(Icons.add), onPressed: () => _startAddNewTransaction(context),),
//     );

// @override
//   Widget build(BuildContext context) {
//     return Container(
//         height: 550,
//         child: this.transactions.isEmpty ? Column(
//           children: <Widget>[
//             Text(
//               'No Transactions added yet!',
// //this is how we use our theme from main.dart file
//               style: Theme.of(context).textTheme.title,
//             ),
// //Used to give some vertical space
//             SizedBox(
//               height: 60,
//             ),
//             Container(
//               height: 400,
// //Use of our image which we had configured
//               child: Image.asset(
//                 'assets/images/waiting.png',
//                 fit: BoxFit.cover,
//               ),
//             ),
//           ],
//         ) :
// //ListView.builder is a way of constructing the list where children’s (Widgets) are built on demand.
//  // However, instead of returning a static widget, it calls a function which can be called multiple times
//  // (based on itemCount ) and it’s possible to return different widget at each call.
//         ListView.builder(
//           itemBuilder: (ctx, index){
//             return Card(
//               elevation: 5,
//               margin: EdgeInsets.symmetric(vertical: 8, horizontal: 5),
//                           child: ListTile(
//                 leading: CircleAvatar(radius: 30,
//                   child: Padding(
//                     padding: const EdgeInsets.all(6.0),
//                     child: FittedBox(child: Text('\$${transactions[index].amount}')),
//                   ),
//                 ),
//                 title: Text(
//                   transactions[index].title,
//                   style: Theme.of(context).textTheme.title,
//                 ),
// //Use of intl library, DateFormat is coming from intl
//                 subtitle: Text(
//                   DateFormat.yMMMd().format(transactions[index].date),
//                 ),
//                 trailing: IconButton(
//                   icon: Icon(Icons.delete),
//                   color: Theme.of(context).errorColor,
//                   onPressed: () => deleteTx(this.transactions[index].id),
//                 ),
//               ),
//             );
//           },
//           itemCount: transactions.length,
//         )
//       );
//   }
// }

// //@required in constructure

//  Transaction({@required this.id, @required this.title, @required this.amount, @required this.date});

//  FlatButton(
//                   child: Text(
//                     'Choose Date',
//                     style: TextStyle(fontWeight: FontWeight.bold),
//                   ),
//                   onPressed: _presentDatePicker,
//                   textColor: Theme.of(context).primaryColor,
//                 ),

//  Card()

//  var myInt = int.parse('12345');
//  You can parse a string into an integer with int.parse(). For example:

// var myInt = int.parse('12345');
// assert(myInt is int);
// print(myInt); // 12345
// Note that int.parse() accepts 0x prefixed strings. Otherwise the input is treated as base-10.

// You can parse a string into a double with double.parse(). For example:

// var myDouble = double.parse('123.45');
//   //this is how we use the variables from the stateful class into its state class
//       widget.addTx(enteredTitle, enteredAmount, _selectedDate);

// FlatButton(
//   color: Colors.blue,
//   textColor: Colors.white,
//   disabledColor: Colors.grey,
//   disabledTextColor: Colors.black,
//   padding: EdgeInsets.all(8.0),
//   splashColor: Colors.blueAccent,
//   onPressed: () {
//     /*...*/
//   },
//   child: Text(
//     "Flat Button",
//     style: TextStyle(fontSize: 20.0),
//   ),
// )
