// import React, { Component } from 'react';
// import logo from './logo.svg';
// import './App.css';
// import autocomplete from './autocomplete';
//
//
// class App extends Component {
//
//
// render() {
//   return (
//     <div className="App">
//       <autocomplete />
//       </div>
//     );
//   }
// }
//
// export default App;
import React from "react";
//import './App.css';
import Autocomplete from "./Autocomplete";
const App = () => {
  return (
    <div className="App">
      <Autocomplete
        options={[
        "Owen", "Geoff", "alice"
        ]}
      />
    </div>
  );
};

export default App;
