export interface Item {
  category_id?: number;
  id?: number;
  title: string;
  description: string;
  price: number;
  post_date?: Date;
  owner?: string;
  category: string;
  likes_count?: number;
  my_or_not?: boolean;
  picture?: string;
}

export const emptyItem = (): Item => {
  return {
    category: '',
    description: '',
    price: 0,
    title: ''
  };
};

export interface IAuthResponse {
  token: string;
}

export interface Category {
  id: number;
  title: string;
}

export interface Comment {
  description: string;
  post_date?: Date;
  author?: string;
}
