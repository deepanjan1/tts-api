import React from 'react';
import {
  StyleSheet,
  View,
} from 'react-native';
import { SafeAreaView } from 'react-navigation'; // ensures title is below notch

// TabNavigator
import TabNavigator from '../navigators/AppNavigator';

import PlaybackControl from '../components/PlaybackControl';

class MainScreen extends React.Component {
  render() {
    return (
      <SafeAreaView style={ styles.container }>
        <TabNavigator />
        <PlaybackControl />
      </SafeAreaView>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-start',
    alignItems: 'stretch',
    backgroundColor: '#F5FCFF',
    marginRight: 5,
    marginLeft: 5,
  },
});

export default MainScreen;
