/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, {Component} from 'react';
import {Platform, StyleSheet, Text, View} from 'react-native';

// importing redux packages
import { Provider, connect } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import logger from 'redux-logger';
import reduxThunk from 'redux-thunk';

// Screen
// import ArticleView from './src/tabs/ArticleView'
import TabNavigator from './src/navigators/AppNavigator'

// Creating store for redux
// const store = createStore(
//   rootReducer,
//   applyMiddleware(reduxThunk));


const instructions = Platform.select({
  ios: 'Press Cmd+R to reload,\n' + 'Cmd+D or shake for dev menu',
  android:
    'Double tap R on your keyboard to reload,\n' +
    'Shake or press menu button for dev menu',
});

export default class App extends React.Component {
  render() {
    // <Text style={styles.welcome}>Welcome to React Native!</Text>
    // <Text style={styles.instructions}>To get started, edit App.js</Text>
    // <Text style={styles.instructions}>{instructions}</Text>
    return <TabNavigator />;
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});
