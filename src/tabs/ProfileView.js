import React from 'react';
import {
  StyleSheet,
  Text,
  View,
} from 'react-native';

export default class ProfileView extends React.Component {
  render () {
    return (
      <View style={styles.container}>
        <Text>ProfileView</Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
});
