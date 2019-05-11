import React from 'react';
import {
  StyleSheet,
  View,
} from 'react-native';
import { SafeAreaView } from 'react-navigation'; // ensures title is below notch

// Main screens loaded in
import TabNavigator from '../navigators/AppNavigator';
import PlaybackControl from '../components/PlaybackControl';

// redux imports
import * as Action from '../actions/actions';
import { connect } from 'react-redux';

class MainScreen extends React.Component {
  constructor(props) {
    super(props);
  };

  render() {
    return (
      <SafeAreaView style={ styles.container }>
        <TabNavigator />
        <PlaybackControl track={ this.props.activeTrack }/>
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

mapStateToProps = (state) => (
  {
    activeTrack: state.tracks.activeTrack,
  }
);

export default connect(mapStateToProps, mapDispatchToProps)(MainScreen);
