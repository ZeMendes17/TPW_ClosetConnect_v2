export interface User {
  id: number;
  username: string;
  name: string;
  email: string;
  password: string;
  admin: boolean;
  image: string;
  description: string;
  sold: number;
  image_base64: string;
}
