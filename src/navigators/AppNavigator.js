import {
  createBottomTabNavigator,
  createAppContainer,
} from 'react-navigation';
import ArticleView from '../tabs/ArticleView';

const TabNavigator = createAppContainer(createBottomTabNavigator({
  Home: { screen: ArticleView },
}));

export default TabNavigator;
