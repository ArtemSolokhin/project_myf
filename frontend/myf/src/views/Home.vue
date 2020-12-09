<template>
  <div class="home">
    <!-- <br>
    <router-link to="add-field" class="btn btn-primary float-right">Add field</router-link>
    <br>
    <b-table striped hover :items="items" :fields="fields">

      <template #cell(controls)="row">
        <b-button size="sm" variant="danger" @click="deleteItem(row.item.id)" class="mr-1">
          Delete
        </b-button>
      </template>

    </b-table> -->
    <h1> Already registered {{ items.length }} users </h1>
    <h1>Register NOW!</h1>
    <router-link to="Registration" class="btn btn-primary">Registration</router-link>
    <h2>Did you have Already Account?</h2>
    <router-link to="SignIn" class="btn btn-primary">SignIn</router-link>
    <div class="container p-3 my-3 border">
      <h2>
      "ManageYourField" will help the site owner in the efficient cultivation of agricultural plants. Data on sites will be processed and presented in a form convenient for work with them. Also, this software system will help users looking for supplies or large batches of crops.
      For them, the system will be a convenient search to find the desired query. This system has no analogues on the market, so it should be well received on it
    </h2>
    <h2>
      Managing your own plot for agricultural purposes is a very difficult task. This is a constant monitoring of the site, which takes a lot of time, and if neglected somewhere, it can lead to big problems. Many people manage on their own, completely doing all the work, and in this case, you can easily forget about something, and this will lead to serious problems. If you are tired of constantly remembering what you have done and what you have not, or you are tired of doing something that can be done in 10 seconds, done in a few hours, then you will have the opportunity to manage your site without feeling that you have forgotten something.
    </h2>
    </div>
  </div>
</template>

<script>
import {config} from "../../config";

export default {
  name: 'Home',
  async mounted() {
    let response = await fetch(config.api_path + 'user/');
    this.items = await response.json();
  },
  data() {
      return {
        items: [],
      }
  },
  
}
</script>
