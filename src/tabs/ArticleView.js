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

import { WebView } from 'react-native-webview';

class ArticleView extends React.Component {
  constructor(props) {
    super(props);
  };

  componentDidMount = () => {
    this.unsubscribeCurrentUserListener = this.props.trackListData();
  };

  componentDidUpdate = (prevProps) => {
    if (prevProps.tracks !== this.props.tracks) {
      console.log(this.props.tracks);
    }
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
    const { tracks, playTrack } = this.props;
    return (
      <SafeAreaView style={ styles.container }>
        <View>
            <Text style={{ textAlign: 'center', marginBottom: 5, }}>Home</Text>
            <Button
              onPress={ () => {
                var dom = authorizePocket();
                return (<WebView source={{ dom }} />);
              }
            }
              title='Login'
            />
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
              <Track track = { item } playTrack = { playTrack }/>
            }
            keyExtractor={ item => item.key }
          />
        </View>
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
  }
);

mapDispatchToProps = (dispatch) => (
  ({
    trackListData: () => {
      dispatch(Action.trackListData());
    },

    playTrack: (track) => {
      dispatch(Action.selectedTrack(track));
    },
  })
);

export default connect(mapStateToProps, mapDispatchToProps)(ArticleView);
