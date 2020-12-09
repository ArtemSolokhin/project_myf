import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import AddField from '../views/AddField'
import UpdateField from '../views/UpdateField'
import Registration from '../views/Registration'
import Profile from '../views/Profile'
import SignIn from '../views/SignIn'


Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/add-field',
    name: 'AddField',
    component: AddField
  },
  {
    path: '/update-field',
    name: 'UpdateField',
    component: UpdateField
  },
  {
    path: '/registration',
    name: 'Registration',
    component: Registration
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router
