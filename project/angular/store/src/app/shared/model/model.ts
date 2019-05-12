export interface Item {
  title: string;
  description: string;
  price: number;
  post_date: Date;
  owner: string;
  category: string;
  like_count: number;
}

export interface IAuthResponse {
  token: string;
}

export interface Category {
  title: string;
}

export interface Comment {
  description: string;
  post_date: Date;
  author: string;
}
