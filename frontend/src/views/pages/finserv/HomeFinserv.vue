<template>
  <div>
    <!-- search input -->
    <section id="knowledge-base-search">
      <b-card
        no-body
        class="knowledge-base-bg text-center"
        :style="{backgroundImage: `url(${require('@/assets/images/banner/banner.png')})`}"
      >
        <b-card-body class="card-body">
          <h2 class="text-primary">
            One place for all your search needs.
          </h2>
          <b-card-text class="mb-2">
            <span>Popular searches: </span>
            <span class="font-weight-bolder">Loans, Insurance & Investments</span>
          </b-card-text>

          <!-- form -->
          <b-form class="kb-search-input">
            <b-input-group class="input-group-merge">
              <b-input-group-prepend is-text>
                <feather-icon icon="SearchIcon" />
              </b-input-group-prepend>
              <b-form-input
                id="searchbar"
                v-model="knowledgeBaseSearchQuery"
                placeholder="Ask a question...."
              />
            </b-input-group>
          </b-form>
          <!-- form -->
        </b-card-body>
      </b-card>
    </section>
    <!--/ search input -->
    <b-row class="container">
      <b-row class="blog-list-wrapper">
        <b-col
          v-for="blog in blogList"
          :key="blog.img"
          md="6"
        >
          <b-card
            tag="article"
            no-body
          >
            <b-link :href="blog.link">
              <b-img
                :src="blog.img"
                class="card-img-top"
              />
            </b-link>
            <b-card-body>
              <b-card-title>
                <b-link
                  :href="blog.link"
                  class="blog-title-truncate text-body-heading"
                >
                  {{ blog.title }}
                </b-link>
              </b-card-title>
              <div class="my-1 py-25">
                <!--                <b-link-->
                <!--                  v-for="(tag,index) in blog.tags"-->
                <!--                  :key="index"-->
                <!--                >-->
                <!--                  <b-badge-->
                <!--                    pill-->
                <!--                    class="mr-75"-->
                <!--                    :variant="tagsColor(tag)"-->
                <!--                  >-->
                <!--                    {{ tag }}-->
                <!--                  </b-badge>-->
                <!--                </b-link>-->
              </div>
              <b-card-text class="blog-content-truncate">
                {{ blog.excerpt }}
              </b-card-text>
              <hr>
              <div class="d-flex justify-content-between align-items-center">
                <b-link
                  :href="blog.link"
                  class="font-weight-bold"
                >
                  Read More
                </b-link>
              </div>
            </b-card-body>
          </b-card>
        </b-col>
        <b-col cols="12">
          <!-- pagination -->
          <div class="my-2">
            <b-pagination
              v-model="currentPage"
              align="center"
              :total-rows="rows"
              first-number
              last-number
              prev-class="prev-item"
              next-class="next-item"
            >
              <template #prev-text>
                <feather-icon
                  icon="ChevronLeftIcon"
                  size="18"
                />
              </template>
              <template #next-text>
                <feather-icon
                  icon="ChevronRightIcon"
                  size="18"
                />
              </template>
            </b-pagination>
          </div>
        </b-col>
      </b-row>
      <section id="knowledge-base-content">
        <!-- content -->
        <b-row class="kb-search-content-info match-height">
          <b-col
            v-for="item in filteredKB"
            :key="item.id"
            md="4"
            sm="6"
            class="kb-search-content"
          >
            <b-card
              class="text-center cursor-pointer"
              :img-src="item.img"
              :img-alt="item.img.slice(5)"
              img-top
              @click="$router.push({ name: 'pages-knowledge-base-category', params: { category: item.category } })"
            >
              <h4>{{ item.title }}</h4>
              <b-card-text class="mt-1">
                {{ item.desc }}
              </b-card-text>
            </b-card>
          </b-col>
          <b-col
            v-show="!filteredKB.length"
            cols="12"
            class="text-center"
          >
            <h4 class="mt-4">
              Search result not found!!
            </h4>
          </b-col>
        </b-row>
      </section>
    </b-row>

  </div>
</template>
<style scoped>
.container{
  margin: auto!important;
}
</style>
<script>
import {
  BRow, BCol, BCard, BCardBody, BForm, BCardTitle, BInputGroup, BFormInput, BCardText, BInputGroupPrepend, BImg, BLink, BPagination,
} from 'bootstrap-vue'
import { kFormatter } from '@core/utils/filter'

export default {
  components: {
    BRow,
    BCol,
    BCard,
    BCardBody,
    BCardText,
    BCardTitle,
    BForm,
    BInputGroupPrepend,
    // BMedia,
    // BAvatar,
    // BMediaAside,
    // BMediaBody,
    BLink,
    BInputGroup,
    BImg,
    BPagination,
    BFormInput,
  },
  data() {
    return {
      knowledgeBaseSearchQuery: '',
      kb: [],
      search_query: '',
      blogList: [
        {
          title: 'How Important Are Credit Card Statements?',
          img: 'http://localhost:8080/images/blog/blog1.jpg',
          link: 'https://www.bajajfinservmarkets.in/credit-card/articles/how-important-are-credit-card-statements.html',
          excerpt: 'Credit Cards have drastically changed the way we look at our finances. Time and again, they have brought premium products within our buying reach and with this, have taught us ',
        },
        {
          title: 'How Important Are Credit Card Statements?',
          img: 'http://localhost:8080/images/blog/blog1.jpg',
          link: 'https://www.bajajfinservmarkets.in/credit-card/articles/how-important-are-credit-card-statements.html',
          excerpt: 'Credit Cards have drastically changed the way we look at our finances. Time and again, they have brought premium products within our buying reach and with this, have taught us ',
        },
        {
          title: 'How Important Are Credit Card Statements?',
          img: 'http://localhost:8080/images/blog/blog1.jpg',
          link: 'https://www.bajajfinservmarkets.in/credit-card/articles/how-important-are-credit-card-statements.html',
          excerpt: 'Credit Cards have drastically changed the way we look at our finances. Time and again, they have brought premium products within our buying reach and with this, have taught us ',
        },
      ],
      blogSidebar: {},
      currentPage: 1,
      perPage: 1,
      rows: 140,

    }
  },
  computed: {
    filteredKB() {
      const knowledgeBaseSearchQueryLower = this.knowledgeBaseSearchQuery.toLowerCase()
      return this.kb.filter(item => item.title.toLowerCase().includes(knowledgeBaseSearchQueryLower) || item.desc.toLowerCase().includes(knowledgeBaseSearchQueryLower))
    },
  },
  created() {
    // this.$http.get('/blog/list/data').then(res => { this.blogList = res.data })
    this.$http.get('/kb/data/knowledge_base').then(res => { this.kb = res.data })
  },
  methods: {
    kFormatter,
    tagsColor(tag) {
      if (tag === 'Quote') return 'light-info'
      if (tag === 'Gaming') return 'light-danger'
      if (tag === 'Fashion') return 'light-primary'
      if (tag === 'Video') return 'light-warning'
      if (tag === 'Food') return 'light-success'
      return 'light-primary'
    },
  },
}
</script>

<style lang="scss">
@import '@core/scss/vue/pages/page-knowledge-base.scss';
</style>
