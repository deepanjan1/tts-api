import {
  createBottomTabNavigator,
  createAppContainer,
} from 'react-navigation';
import ArticleView from '../tabs/ArticleView';
import PlaylistView from '../tabs/PlaylistView';
import ProfileView from '../tabs/ProfileView';

const TabNavigator = createAppContainer(createBottomTabNavigator({
  Home: { screen: ArticleView },
  Playlist: { screen: PlaylistView },
  Profile: { screen: ProfileView },
},
{
  tabBarOptions: {
    labelStyle: {
      fontSize: 12,
    },
    tabStyle: {
      height: 20,
    },
    style: {
      height: 10,
    },
  },
}
));

export default TabNavigator;
