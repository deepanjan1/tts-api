import React from 'react';
import {
  StyleSheet,
  Text,
  View,
  FlatList,
  Image,
  Button,
} from 'react-native';
import { SafeAreaView } from 'react-navigation'; // ensures title is below notch
import { SearchBar } from 'react-native-elements'; // Search bar

import Track from '../components/Track'; // Import track component

import { authorizePocket } from '../utilities/pocketAuth.js'; // Import pocket auth function

// redux imports
import * as Action from '../actions/actions';
import { connect } from 'react-redux';

class ArticleView extends React.Component {
  constructor(props) {
    super(props);
  };

  componentDidMount = () => {
    this.unsubscribeCurrentUserListener = this.props.trackListData();
  };

  // adding a dummy state
  state = {
    search: '',
  };

  updateSearch = search => {
    this.setState({ search });
  };

  render () {
    const { search } = this.state;
    const { tracks } = this.props;
    console.log(tracks);
    return (
      <View style={ styles.container }>
        <SafeAreaView>
          <Text style={{ textAlign: 'center', marginBottom: 5, }}>Home</Text>
          <Button
            onPress={ () => authorizePocket() }
            title='Login'
          />
        </SafeAreaView>
        <View>
          <SearchBar
            placeholder="Type Here..."
            onChangeText={this.updateSearch}
            value={search}
            Icon={ null }
            searchIcon={ null }
          />
        </View>
        <View style={ styles.horizontalRule } />
        <FlatList
          data={ tracks }
          renderItem={({ item }) =>
            <Track track = { item } />
          }
        />
      </View>
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
  horizontalRule: {
    marginTop: 5,
    marginBottom: 5,
    borderBottomColor: 'black',
    borderBottomWidth: 1,
  },
});

mapStateToProps = (state) => (
  {
    tracks: state.tracks.tracks,
    activeTrack: state.tracks.activeTrack,
  }
);

mapDispatchToProps = (dispatch) => (
  ({
    trackListData: () => {
      dispatch(Action.trackListData());
    },
  })
);

export default connect(mapStateToProps, mapDispatchToProps)(ArticleView);
