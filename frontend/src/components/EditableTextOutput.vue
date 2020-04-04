<template>
  <div class="host">
    <div v-if="!editMode">
        <span v-if="!editMode">{{ localValue }}</span>
        <button class="no-optic" v-on:click="startEditMode" type="button">
            <svg class="bi bi-pencil" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M11.293 1.293a1 1 0 011.414 0l2 2a1 1 0 010 1.414l-9 9a1 1 0 01-.39.242l-3 1a1 1 0 01-1.266-1.265l1-3a1 1 0 01.242-.391l9-9zM12 2l2 2-9 9-3 1 1-3 9-9z" clip-rule="evenodd"/>
                <path fill-rule="evenodd" d="M12.146 6.354l-2.5-2.5.708-.708 2.5 2.5-.707.708zM3 10v.5a.5.5 0 00.5.5H4v.5a.5.5 0 00.5.5H5v.5a.5.5 0 00.5.5H6v-1.5a.5.5 0 00-.5-.5H5v-.5a.5.5 0 00-.5-.5H3z" clip-rule="evenodd"/>
            </svg>
        </button>
    </div>
    <div v-if="editMode">
      <input v-if="type === 'input'" v-model="localValue" v-on:keyup.escape="cancelChange" v-on:keyup.enter="saveChange" />
      <textarea v-if="type === 'textarea'" :rows="rows" :cols="cols" v-model="localValue" v-on:keyup.escape="cancelChange" />
      <button v-on:click="saveChange" type="button">
        <svg class="bi bi-check" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M13.854 3.646a.5.5 0 010 .708l-7 7a.5.5 0 01-.708 0l-3.5-3.5a.5.5 0 11.708-.708L6.5 10.293l6.646-6.647a.5.5 0 01.708 0z" clip-rule="evenodd"/>
        </svg>
      </button>
      <button v-on:click="cancelChange" type="button">
        <svg class="bi bi-x" width="1em" height="1em" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M11.854 4.146a.5.5 0 010 .708l-7 7a.5.5 0 01-.708-.708l7-7a.5.5 0 01.708 0z" clip-rule="evenodd"/>
            <path fill-rule="evenodd" d="M4.146 4.146a.5.5 0 000 .708l7 7a.5.5 0 00.708-.708l-7-7a.5.5 0 00-.708 0z" clip-rule="evenodd"/>
        </svg>
      </button>
    </div>
  </div>
</template>

<style scoped>

svg {
  width: 70%;
}

button.no-optic {
  border: 0;
  margin-left: 0.3em;
}

div.host {
  display: inline-block;
  display: inline.flex;
}

input {
  min.width: 200px;
}
</style>

<script>
export default {
  props: {
    value: {
      type: String,
      default: 'n/a'
    },
    type: {
      type: String,
      default: 'input'
    },
    cols: {
      type: Number,
      default: 80
    },
    rows: {
      type: Number,
      default: 10
    }
  },
  watch: {
    value () {
      this.localValue = this.value
    }
  },
  mounted: function () {
    this.localValue = this.value
  },
  data: function () {
    return {
      localValue: undefined,
      editMode: false
    }
  },
  methods: {
    startEditMode: function (event) {
      this.editMode = true
      console.log(this.$refs.inputElement)
    },
    saveChange: function (event) {
      this.editMode = false
      this.$emit('input', this.localValue)
      this.$emit('change')
    },
    cancelChange: function (event) {
      this.localValue = this.value
      this.editMode = false
    }
  }
}
</script>
