<template>
  <div class="home">
    <br>
    <router-link to="add-field" class="btn btn-primary float-right">Add field</router-link>
    <br>
    <b-table striped hover :items="items" :fields="fields">

      <template #cell(controls)="row">
        <b-button size="sm" variant="danger" @click="deleteItem(row.item.id)" class="mr-1">
          Delete
        </b-button>
      </template>

    </b-table>
  </div>
</template>

<script>
import {config} from "../../config";

export default {
  name: 'Home',
  async mounted() {
    let response = await fetch(config.api_path + 'field/');
    this.items = await response.json();
  },
  data() {
      return {
          fields: [{
              key: 'owner_desc.username',
              label: 'Owner'
          }, {
              key: 'length'
          }, {
              key:  'width'
          }, {
              key: 'controls'
          }],
          items: []
      }
  },
  methods: {
      deleteItem: function (id) {
        fetch(config.api_path + 'field/' + id + '/', {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          }
        }).then(async () => {
            let response = await fetch(config.api_path + 'field/');
            this.items = await response.json();
        });
      }
  }
}
</script>
